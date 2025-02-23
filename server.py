import sys
from flask import Flask, send_file, render_template, send_from_directory

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Disable caching

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = f'static/files/{filename}'
    return send_file(file_path, as_attachment=True)

@app.route('/image/<filename>')
def download_image(filename):
    file_path = f'static/images/{filename}.jpg'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    port = 8000
    ip_addr = '127.0.0.1'
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]
    
    app.run(debug=True, port=port, host=ip_addr)