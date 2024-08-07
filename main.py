from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='client/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else: return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()
# Test
