from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to My Website</h1><p>This is a simple Flask web page.</p>'


if __name__ == '__main__':
    app.run(debug=True)
