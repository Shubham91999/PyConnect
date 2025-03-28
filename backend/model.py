# Importing the SQLAlchemy db model that we created in config file
from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False, unique=False)
    second_name = db.Column(db.String(80), nullable=False, unique=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "secondName": self.second_name,
            "email": self.email
        }
