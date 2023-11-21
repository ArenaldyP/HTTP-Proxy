# Skrip Manipulasi HTML mitmproxy
Skrip Python ini memperlihatkan cara menggunakan mitmproxy untuk memanipulasi lalu lintas HTTP/HTTPS dengan menyisipkan elemen HTML dan JavaScript ke dalam respons. Ideal untuk uji coba dan eksperimen, skrip ini menambahkan tampilan overlay ke halaman HTML yang diterima, menciptakan efek visual dan menampilkan pesan peringatan.

## Fitur Utama
* Overlay_HTML: Elemen HTML yang dienkripsi dalam bentuk byte, berupa gambar semi-transparan dengan posisi tetap, ditambahkan ke halaman HTML.
* Overlay_JS: Skrip JavaScript yang dienkripsi dalam bentuk byte, menampilkan pesan peringatan dan meningkatkan manipulasi interaktif.

## Cara Penggunaan
* sudo apt install mitmproxy
* mitmproxy --ignore '^(?!duckduckgo\.com)' -s HTTP_Proxy.py
* sudo iptables -t nat -A OUTPUT -p tcp --match multiport --dports 80,443 -j REDIRECT --to-ports 8080

## Isi yang Disisipkan:
* Overlay gambar dengan posisi tetap untuk menciptakan efek visual.
* Pesan peringatan JavaScript yang memberitahu pengguna bahwa interaksi di halaman dinonaktifkan.

## Note
Hormati pertimbangan etika, dapatkan izin yang diperlukan, dan patuhi hukum yang berlaku saat menggunakan alat manipulasi lalu lintas ini.
Jelajahi potensi mitmproxy untuk pengujian, debugging, dan memahami bagaimana aplikasi web menangani respons yang dimanipulasi. Tingkatkan kreativitas dan perbaiki alur kerja pengembangan Anda dengan memanfaatkan skrip ini.

## Disclaimer
Pastikan penggunaan etis dan patuhi kebijakan dan hukum yang berlaku. Manipulasi yang tidak sah dapat melanggar syarat layanan atau peraturan hukum. Gunakan dengan tanggung jawab dan hanya pada sistem yang diizinkan untuk diuji.
Anda dapat menyesuaikan dan memperluas skrip ini sesuai kebutuhan Anda!

