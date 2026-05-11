from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "test83298r23089jfi32jm4iognmiog9023tjnm Hello EPSIC 158! - Modifié automatiquement par Jenkins ! "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
