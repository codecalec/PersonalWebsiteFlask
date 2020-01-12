from flask import render_template
from app import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", home_active=True)


@app.route("/blog")
def blog():
    return render_template("blog.html", blog_active=True)


@app.route("/resume")
def resume():
    from urllib.request import urlopen
    from markdown import markdown

    with urlopen(
        "https://alexveltmanpersonalwebsite.s3.eu-west-2.amazonaws.com/markdown/resume.md"
    ) as f:
        contents = markdown(f.read().decode("utf-8"))

    return render_template("resume.html", resume_active=True, text=contents)
