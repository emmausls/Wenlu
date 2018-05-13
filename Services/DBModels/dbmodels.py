from Services import db

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    mobilephone = db.Column(db.Integer,unique=True)
    email = db.Column(db.String(128),unique=True)
    username = db.Column(db.String(128),unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__=='__main__':
    db.create_all()