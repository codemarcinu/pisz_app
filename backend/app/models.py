from . import db

class Paragony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    sklep = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)

class Produkty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    # Add other product fields