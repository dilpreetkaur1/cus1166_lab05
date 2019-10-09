from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__= "courses"

    id = db.Column(db.Integer,primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    student = db.relationship("Registered Student", backref="Courses", lazy=True)

def add_grade(self,name,grade):

    new_student = registeredStudent(name=name, grade=grade , course_id=self.id )
    db.session.add(new_student)
    db.session.commit()

class registeredStudent(db.Model):
    __tablename__ = "Registered Student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.String, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)