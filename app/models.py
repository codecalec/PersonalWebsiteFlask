from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    text_location = db.Column(db.String())
    date = db.Column(db.Date())

    def __repr__(self):
        return '<id {}>'.format(self.id)

