from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
import datetime

db = SQLAlchemy()


class People(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 checked = db.Column(db.Boolean)
 name = db.Column(db.String(80))
 type = db.Column(db.String(80))
 age = db.Column(db.Integer)
 description = db.Column(db.String(256)) 
 datetime = db.Column(db.String(80)) 

 def __repr__(self):
  pass

 def __init__(self, checked, name, type, age, description):
  self.checked = checked
  self.name = name
  self.type = type
  self.age = age
  self.description = description

     


   








































# import sqlite3


# conn = sqlite3.connect('test.db')
# print("Opened database successfully")

# conn.execute('''CREATE TABLE COMPANY
#          (ID          INTEGER  PRIMARY KEY AUTOINCREMENT   NOT NULL ,
#          CHECKED      BOOLEAN             NOT NULL,
#          NAME         CHAR(50)            NOT NULL,
#          TYPE         CHAR(50)            NOT NULL,
#          AGE          NUMERIC             NOT NULL,
#          DESCRIPTION  CHAR(256)           NOT NULL,
#          DATE         DATETIME           NOT NULL);''')

# conn.close()


# print("Table created successfully")



# conn.execute("INSERT INTO COMPANY (ID,CHECKED,NAME,TYPE,AGE,DESCRIPTION,DATE) \
#       VALUES (1, 0, 'UDAY', 'HELLO', 23, 'shadiuashduisahdiuas', '2022-12-25 06:25:25.256')")


# conn.commit()
