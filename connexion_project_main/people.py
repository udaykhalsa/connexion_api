# from dbconnect import get_people_db
import sqlite3
import json
import datetime

from db_query import *
from flask import request


# @application.route('/people/{id}', methods=['POST','GET'])
def get_people(id):
  results = get_people_db(id)
  return json.dumps(results)


def post():
  data = request.get_json()

  checked = data.get("checked")
  name = data.get("name")
  type = data.get("type")
  age = data.get("age")
  description = data.get("description")
  date = datetime.datetime.now()

  create_people_db(checked, name, type, age, description, date)
      

def put(id):
  data = request.get_json()
  
  id = id
  checked = data.get("checked")
  name = data.get("name")
  type = data.get("type")
  age = data.get("age")
  description = data.get("description")
  date = datetime.datetime.now()

  update_people_db(checked, name, type, age, description, date)



def delete(id):
  delete_people_db(id)
