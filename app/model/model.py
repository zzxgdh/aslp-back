
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class student(db.Model):
    name = db.Column(db.String(80),primary_key=True,nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    def toString(self):
        return self.name+" "+self.gender

