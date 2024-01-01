from flask import Flask, request, jsonify
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# [BASIC FLASK API]
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     return "Home"
#
# @app.route("/user/<user_id>")
# def getUser(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Ji-Woong Hwang",
#         "email": "carrenddda@naver.com"
#     }
#
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#
#     return jsonify(user_data), 200
#
# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()
#
#     return jsonify(data),201
#
# if __name__ == "__main__":
#     app.run(debug=True)


# [FLASK WITH ALCHEMY]
Base = declarative_base()


class Person(Base):
    __tablename__ = "member"

    ssn = Column("ssn", Integer, primary_key=True)
    firstName = Column("firstname", String)
    lastName = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstName = first
        self.lastName = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstName} {self.lastName} ({self.gender}, {self.age})"


engine = create_engine("sqlite:///testdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(123, "jiwoong", "Hwang", "M", 35)
# session.add(person)
# session.commit()


results = session.query(Person).all()

print(results)
