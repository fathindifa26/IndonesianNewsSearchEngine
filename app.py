import pickle
import numpy as np
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
import re
import pandas as pd

# Fungsi untuk melakukan tokenisasi teks
def tokenize_text(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

# Fungsi untuk memuat model dan embedding
def load_embeddings(filename="embeddings.pkl"):
    with open(filename, "rb") as file:
        data = pickle.load(file)
    return data["W1"], data["word2idx"], data["vocab"]

# Fungsi untuk mendapatkan embedding dokumen
def get_document_embedding(doc_tokens, word2idx, W1, embedding_dim):
    embedding = np.zeros(embedding_dim)  # Inisialisasi vektor embedding untuk dokumen
    valid_word_count = 0  # Untuk menghitung jumlah kata valid
    for word in doc_tokens:
        if word in word2idx:
            word_idx = word2idx[word]  # Mendapatkan indeks kata
            embedding += W1[word_idx]  # Menambahkan embedding kata ke embedding dokumen
            valid_word_count += 1
    return embedding / valid_word_count if valid_word_count > 0 else embedding


# Fungsi untuk mencari dokumen yang paling relevan
def search(query, df, word2idx, W1, embedding_dim=100, top_n=3):
    query_tokens = query.lower().split()  # Tokenisasi query
    query_embedding = get_document_embedding(query_tokens, word2idx, W1, embedding_dim)

    doc_embeddings = []
    for _, row in df.iterrows():
        doc_tokens = row['content'].lower().split()  # Tokenisasi dokumen
        doc_embedding = get_document_embedding(doc_tokens, word2idx, W1, embedding_dim)
        doc_embeddings.append(doc_embedding)

    similarities = cosine_similarity([query_embedding], doc_embeddings)
    top_n_idx = np.argsort(similarities[0])[::-1][:top_n]

    # Mengembalikan data dalam format tabel
    return [
        {
            "no": i + 1,
            "title": df.iloc[idx]['title'],
            "url": df.iloc[idx]['url'],
            "similarity": similarities[0][idx]
        }
        for i, idx in enumerate(top_n_idx)
    ]


# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Load embeddings saat aplikasi dijalankan
W1, word2idx, vocab = load_embeddings(filename="embeddings.pkl")
embedding_dim = W1.shape[1]

# Load DataFrame berita
df = pd.read_csv('data.csv')  # Pastikan data.csv memiliki kolom 'title' dan 'content'
df.dropna(inplace=True)

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint untuk pencarian
@app.route('/search', methods=['POST'])
def search_results():
    query = request.form['query']
    results = search(query, df, word2idx, W1, top_n=5)
    return render_template('index.html', query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
