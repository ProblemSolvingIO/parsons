from datetime import datetime

from parsons import db


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.DateTime(), nullable=False,
                      default=datetime.utcnow)
    title = db.Column(db.Text(), nullable=False)
    code = db.Column(db.Text(), nullable=False)
    url = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return '<Program %r>' % self.title
