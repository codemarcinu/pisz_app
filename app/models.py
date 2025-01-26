from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, default=0)

class Paragon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sklep = db.Column(db.String(128), nullable=False)
    data = db.Column(db.Date, nullable=False)
    laczna_cena = db.Column(db.Float, nullable=False)
    rabat = db.Column(db.Float, default=0.0)