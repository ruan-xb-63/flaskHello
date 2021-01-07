from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def print_hi(name):
    serverSay = f'Hi, {name}'
    return serverSay

if __name__ == '__main__':
    app.run(port=5008)
