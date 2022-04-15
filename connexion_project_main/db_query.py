import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_people_db(id):
 conn = sqlite3.connect('test.db', check_same_thread=False)
 conn.row_factory = dict_factory
 cursor = conn.cursor()
 cursor = cursor.execute(f"SELECT * from COMPANY where ID == {id}")
 results = cursor.fetchone()

 conn.close()
 return results

def create_people_db(checked, name, type, age, description, date):
  conn = sqlite3.connect('test.db', check_same_thread=False)

  conn.execute(f"INSERT INTO COMPANY (CHECKED,NAME,TYPE,AGE,DESCRIPTION,DATE) \
      VALUES ({checked}, {name}, {type}, {age}, {description}, {date})")

  conn.commit()


def update_people_db(id, checked, name, type, age, description, date):
  conn = sqlite3.connect('test.db', check_same_thread=False)

  conn.execute(f"UPDATE COMPANY set NAME = {name}, CHECKED = {checked}, TYPE = {type}, AGE = {age}, DESCRIPTION = {description}, DATE = {date}) where ID = {id}")

  conn.commit()

  conn.close()
  

def delete_people_db(id):
  conn = sqlite3.connect('test.db', check_same_thread=False)

  conn.execute(f"UPDATE from COMPANY where ID = {id}")

  conn.commit()

  conn.close()