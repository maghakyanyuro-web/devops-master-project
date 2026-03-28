from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Laurik jan bacatrem , sa cragir e grvac Yuroi koxmic, zarmacac es ete ayo greq instagram-in😂😂👌"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
