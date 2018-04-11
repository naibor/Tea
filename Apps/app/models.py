from Apps.app import db

class User (db.Model):
    # fields are instances of the db.column 
    # the field type,unique and index as an argument 
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        # this method tells python how to print objects of this class
        return '<User %r>' %(self.nickname)
