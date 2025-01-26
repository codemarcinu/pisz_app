from zakupy_app.extensions import db

class Kategorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)

class Produkty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(255), nullable=False)
    kategoria_id = db.Column(db.Integer, db.ForeignKey('kategorie.id'))
    czy_zamrozone = db.Column(db.Boolean, default=False)
    data_waznosci = db.Column(db.Date)

class Paragony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    sklep = db.Column(db.String(100), nullable=False)
    laczna_cena = db.Column(db.Float)
    rabat = db.Column(db.Float)