from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    port = 9100  # Default port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    app.run(host='0.0.0.0', port=port)
