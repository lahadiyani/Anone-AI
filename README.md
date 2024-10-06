# Dokumentasi Proyek Anone AI

## Deskripsi Proyek
Proyek ini adalah aplikasi web sederhana yang memungkinkan pengguna untuk menghasilkan gambar berdasarkan prompt yang diberikan menggunakan API model machine learning. Pengguna dapat memasukkan prompt dan API key untuk mengakses model yang diinginkan.

![icons](https://github.com/lahadiyani/Anone-AI/blob/main/static/image/icons.png)

## Fitur Utama
- Menghasilkan gambar berdasarkan input prompt.
- Menyimpan gambar yang dihasilkan ke dalam folder `static/output/`.
- Menampilkan gambar di halaman web setelah dihasilkan.
- Menangani kesalahan jika gambar tidak dapat dihasilkan.

## Struktur Proyek
```
/your-project
│
├── app/                   # Folder yang berisi modul aplikasi.
│   ├── __init__.py        # Inisialisasi aplikasi Flask.
│   ├── route.py           # Rute aplikasi untuk menangani permintaan.
│   ├── utils.py           # Modul untuk fungsi utilitas, termasuk query API.
│   └── config.py          # Modul untuk konfigurasi aplikasi.
│
├── static/ 
│   ├── css/               # Folder untuk file CSS.
│   ├── js/                # Folder untuk file JavaScript.
│   └── output/            # Folder untuk menyimpan gambar yang dihasilkan.
│
├── templates/             # Folder yang berisi template HTML.
│   └── index.html         # Template HTML untuk antarmuka pengguna.
│
├── .env-example            # Contoh file untuk konfigurasi variabel lingkungan.
└── app.py                 # File utama untuk menjalankan aplikasi Flask.
```

## Dependensi
Proyek ini membutuhkan beberapa dependensi. Pastikan untuk menginstalnya dengan menggunakan `pip`:

```bash
pip install Flask Pillow requests python-dotenv
```

## Konfigurasi

```plaintext
API_URL=YOUR_API_URL_HERE
API_KEY=YOUR_API_KEY_HERE
apikey=custom
```

## Cara Menjalankan Proyek
1. **Clone Repository**: Jika proyek ada di repository, clone ke mesin lokal kamu.
   
2. **Instal Dependensi**: Buka terminal dan navigasikan ke direktori proyek, kemudian jalankan perintah berikut untuk menginstal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**: Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah berikut:
   ```bash
   python app.py
   ```
   
4. **Akses Aplikasi**: Buka browser dan pergi ke `http://127.0.0.1:3000/` untuk mengakses aplikasi.

## Penggunaan
- Masukkan prompt pada input yang disediakan.
- Masukkan API key untuk mengakses endpoint.
- Klik tombol untuk menghasilkan gambar.
- Gambar yang dihasilkan akan ditampilkan di bawah input setelah proses selesai.

## Penanganan Kesalahan
- Jika prompt tidak dimasukkan, pengguna akan menerima pesan kesalahan "Prompt is required".
- Jika gambar tidak dapat dihasilkan, pesan kesalahan "No image data returned" akan ditampilkan.
- Jika model masih dalam proses loading, pengguna akan melihat estimasi waktu yang diperlukan.

## Catatan
- Pastikan folder `static/output/` sudah ada dan dapat ditulisi oleh aplikasi untuk menyimpan gambar yang dihasilkan.
- Jika model tertentu tidak aktif atau tidak cukup digunakan, mungkin ada waktu loading yang lebih lama. Pertimbangkan untuk menggunakan model lain jika masalah ini terus berlanjut.
```

##cara mendapatkan API_URL dan API_KEY
[huggingface apikey](https://huggingface.co/settings/tokens) dan contoh apiurl [huggingface api_url](https://huggingface.co/black-forest-labs/FLUX.1-dev) bisa diambil dari viewcode

untuk caranya bisa cek folder asset
