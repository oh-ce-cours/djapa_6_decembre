from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/<username>")
def profile(username):
    profiles = {
        "matthieu": {"skills": ["python", "data science", "dev web"]},
        "philippe": {"skills": ["python", "CPL moyenne tension"]},
    }
    if username in profiles:
        """skills for {{ username }}:
        <ul>
        {% for skill in skills %}
            <li>{{ skill }}</li>
        {% endfor %}
        </ul>
        """

        skills = "".join(
            ["<li>" + skill + "</li>" for skill in profiles[username]["skills"]]
        )
        return f"skills for {username}: <ul>{skills}</ul>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898, debug=True)
