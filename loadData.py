#!/usr.bin/python3
import pymysql

def load_owners(cursor):
  owners_data=open('owners.csv','r')
  for rowline in owners_data:
    row=rowline.rstrip().split(',')
    print(row)
    sql = "INSERT INTO owners (name, gender, phone) VALUES (%s, %s, %s);"
    cursor.execute(sql, row)
  cursor.execute("SELECT * FROM owners;")
  print(cursor.fetchall())

def load_pets(cursor):
  pets_data=open('pets.csv', 'r')
  for rowline in pets_data:
    row=rowline.rstrip().split(',')
    sql = "INSERT INTO pets(owner_id,name,gender,species,color,age) VALUES(%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql, row)
  cursor.execute("SELECT * FROM pets;")
  print(cursor.fetchall())
if __name__ == "__main__":
  db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='creative_online_school')
  cursor = db.cursor()
  load_owners(cursor)
  load_pets(cursor)
  db.commit()
  db.close()
