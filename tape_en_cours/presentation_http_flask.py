from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/<username>")
def profile(username):
    {
        "matthieu": {"skills": ["python", "data science", "dev web"]},
        "philippe": {"skills": ["python", "CPL moyenne tension"]},
    }

    return f"{username}'s profile"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898)
