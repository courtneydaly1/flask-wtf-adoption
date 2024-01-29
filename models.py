from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE= "https://t3.ftcdn.net/jpg/02/73/16/24/360_F_273162497_ShAAB1TH0vhM4UUWbhBuao8jtGBDubwD.jpg"


db= SQLAlchemy()

class Pet(db.Model):
    """ Pets for adoption """
    
    __tablename__='pets'
    
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text, nullable=False)
    species= db.Column(db.Text, nullable=False)
    photo_url= db.Column(db.Text)
    age= db.Column(db.Integer)
    notes= db.Column(db.Text)
    available= db.Column(db.Boolean, nullable=False, default=True)
    
    def image_url(self):
        return self.photo_url or DEFAULT_IMAGE
    
def connect_db():
    """connect this db to flask app"""
    
    db.app =app
    db.init_app(app)
    