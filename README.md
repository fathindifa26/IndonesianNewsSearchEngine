# Indonesian News Search Engine

Program search engine ini menggunakan dataset yang menggabungkan informasi dari tujuh platform berita Indonesia terkemuka: 

- Tempo
- CNN Indonesia
- CNBC Indonesia
- Okezone
- Suara
- Kumparan
- JawaPos

Search engine ini dibangun dengan teknik **word2vec** menggunakan 100 dimensi embeddings untuk menghasilkan pencarian yang lebih relevan dan semantik. Dengan menggunakan teknik ini, sistem dapat memahami hubungan semantik antar kata, sehingga menghasilkan hasil pencarian yang lebih tepat berdasarkan konteks dan kesamaan makna, bukan hanya kecocokan kata kunci secara harfiah.

## Fitur Utama
- **Dataset**: Menggunakan informasi terkini dari tujuh platform berita Indonesia.
- **Word2Vec Embeddings**: Menerapkan model **word2vec** dengan dimensi 100 untuk menghasilkan representasi kata dalam bentuk vektor yang lebih semantik.
- **Pencarian Relevan**: Menyediakan hasil pencarian berdasarkan kedekatan semantik, bukan hanya kecocokan kata.
- **User-Friendly**: Antarmuka yang mudah digunakan untuk mencari berita berdasarkan kata kunci.

## Cara Menggunakan
1. Masukkan kata kunci pencarian pada kolom yang tersedia di halaman utama.
2. Klik tombol **Search** untuk mendapatkan hasil pencarian.
3. Hasil pencarian akan menampilkan judul, URL, dan tingkat kemiripan setiap artikel dengan kata kunci yang dimasukkan.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama untuk backend.
- **Flask**: Framework untuk membuat aplikasi web.
- **Word2Vec**: Untuk menghasilkan embedding kata berbasis konteks.
- **Pandas**: Untuk pengolahan data dan manipulasi dataset.
- **Sklearn**: Untuk mengukur kemiripan antara dokumen menggunakan cosine similarity.

## Instalasi dan Pengaturan
1. **Clone repository**:
    ```bash
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

2. **Install dependensi**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi**:
    ```bash
    python main.py
    ```

4. Buka aplikasi di browser Anda di `http://127.0.0.1:5000`.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, Anda dapat melakukan **fork** repository ini, kemudian mengirimkan **pull request** dengan perubahan atau fitur baru yang ingin Anda tambahkan.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Lihat [LICENSE](LICENSE) untuk informasi lebih lanjut.
