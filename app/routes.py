from flask import render_template
from app import app
from app.models import Post

from sqlalchemy import desc
from urllib.request import urlopen
from markdown import markdown


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", home_active=True)


@app.route("/blog")
def blog():
    postlist = Post.query.order_by(desc(Post.date)).all()
    return render_template("blog.html", postlist=postlist, blog_active=True)


@app.route("/blog/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", post=post, blog_active=True)


@app.route("/resume")
def resume():

    with urlopen(
        "https://alexveltmanpersonalwebsite.s3.eu-west-2.amazonaws.com/markdown/resume.md"
    ) as f:
        contents = markdown(f.read().decode("utf-8"))

    return render_template("resume.html", resume_active=True, text=contents)
