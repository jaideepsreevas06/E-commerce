from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<img src="/static/products/banana.jpeg">'

if __name__ == '__main__':
    app.run(debug=True)