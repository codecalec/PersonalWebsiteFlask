from flask import render_template
from app import app, cache
from app.models import Post
from pathlib import Path

from sqlalchemy import desc
from urllib.request import urlopen
from markdown import markdown

AWS_URL = Path("")


@app.route("/")
@app.route("/home")
@cache.cached(timeout=50)
def home():
    return render_template("home.html", home_active=True)


@app.route("/blog")
@cache.cached(timeout=120)
def blog():
    postlist = Post.query.order_by(desc(Post.date)).all()
    return render_template("blog.html", postlist=postlist, blog_active=True)


@app.route("/blog/<int:post_id>")
@cache.cached(timeout=120)
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", post=post, blog_active=True)


@app.route("/resume")
@cache.cached()
def resume():
    with urlopen(
        "https://alexveltmanpersonalwebsite.s3.eu-west-2.amazonaws.com/markdown/resume.md"
    ) as f:
        contents = markdown(f.read().decode("utf-8"))

    return render_template("resume.html", resume_active=True, text=contents)
