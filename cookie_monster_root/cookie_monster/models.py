from . import db

class Cookie(db.Model):
    __tablename__ = 'cookies'
    pk = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(128))
    name = db.Column(db.String(128))
    value = db.Column(db.String(512))
    
