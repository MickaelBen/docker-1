from flask import Flask



app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"

@app.route("/check-chapter")
def check_chapter():
    return "Hello world"


if __name__ == "__main__":
    app.run(host="192.168.11.10", port=8000)