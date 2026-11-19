# Sistem Pendukung Keputusan Percepatan Masa Studi

Proyek Streamlit untuk penelitian Sumiati, Magister Ilmu Komputer Universitas Pakuan. Titik masuknya adalah `app.py`. Streamlit menampilkan aplikasi interaktif dari `sistem.html`. Pemrosesan CSV dan penskoran dilakukan dalam peramban pengguna.

## Menjalankan di Windows

1. Ekstrak ZIP ke satu folder. Pastikan app.py, sistem.html, dan requirements.txt berada dalam folder yang sama.
2. Dengan Python 3.12 terpasang, buka Terminal di folder tersebut dan jalankan perintah berikut.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

3. Buka alamat Local URL yang ditampilkan di Terminal, biasanya http://localhost:8501. Gunakan Ctrl+C di Terminal untuk menghentikan server.

## Menerapkan di Streamlit Community Cloud

1. Buat repositori GitHub dan unggah isi ZIP yang sudah diekstrak. Letakkan app.py, requirements.txt, dan sistem.html di tingkat paling atas repositori. Pastikan huruf kecil pada nama sistem.html sama persis.
2. Masuk ke https://share.streamlit.io dengan akun yang memiliki akses ke repositori. Pilih **Create app**, lalu **Yup, I have an app**.
3. Pilih repositori dan cabang yang berisi berkas, misalnya main. Isi **Main file path** dengan app.py. Di **Advanced settings**, pilih Python 3.12. Klik **Deploy**.
4. Bila file berada di dalam subfolder, sesuaikan Main file path, misalnya streamlit_sumiati/app.py, dan letakkan requirements.txt serta sistem.html di sebelah app.py.

Panduan resmi: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Mencoba sistem

Klik **Coba data simulasi**. Pada Ringkasan akan tampil 18 respons sintetis dan 19 hasil hipotesis contoh. Buka **Prioritas dan aksi**, pilih indikator, isi rencana tindak lanjut, lalu ekspor hasil ke CSV. File hasil simulasi diberi penanda Simulasi.

Untuk data penelitian, pilih **Mulai penelitian baru**. Pada **Instrumen dan data**, unduh templat, lengkapi satu ID samaran dan 214 jawaban asli per responden, lalu impor CSV. Gunakan ekspor skor terkoreksi sebagai masukan SmartPLS. Jalankan estimasi dan bootstrap di SmartPLS, kemudian salin hasilnya ke templat 19 jalur di menu **Model PLS-SEM**. Di **Prioritas dan aksi**, impor pemetaan butir yang telah disahkan, unduh templat CBUI, lalu masukkan skor konsensus pakar. Menu **Metode sistem** menjelaskan rumus prioritas dan asumsi prototipe.

Simpan file masukan dan ekspor hasil sebelum menutup atau memuat ulang aplikasi. Sesi tidak memakai basis data bersama. Untuk deploy, cukup unggah berkas proyek ke GitHub. Data respons penelitian diimpor melalui aplikasi saat digunakan.
