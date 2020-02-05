from app import db
from urllib.request import urlopen
import markdown


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    text_location = db.Column(db.String())
    date = db.Column(db.Date())

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def get_text(self):
        with urlopen(self.text_location) as f:
            md = markdown.Markdown(extensions=['mdx_math'])
            contents = md.convert(f.read().decode("utf-8"))
        return contents
