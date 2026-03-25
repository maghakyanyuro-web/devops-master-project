from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>DevOps Master Project is LIVE!🥳🥳💻🔥</h1><p>Running on Docker & AWS</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
