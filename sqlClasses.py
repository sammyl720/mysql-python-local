import pymysql
from pymysql import cursors

class Datab():
  def __init__(self, databaseName, host, user, passwd):
    try:
      self.n = databaseName
      self.db = pymysql.connect(host=host, user=user, passwd=passwd)
      self.cursor = self.db.cursor()
      self.cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(self.n))
      self.cursor.execute("USE {};".format(self.n))
      print("Connected to database {0}".format(self.n))
    except pymysql.Error as e:
      print(e)
      print("Unable to connect to database")
  
  def addTable(self, tableName, **columns):
    sql="CREATE TABLE IF NOT EXISTS " + tableName + "("
    for c, t in columns.items():
      sql += "%s %s, " % (c, t)
    sql = sql[:-2]+")"
    self.cursor.execute(sql)
    self.db.commit()
    print("Table {0} created".format(tableName))
  
  def addElement(self, tableName, **values):
    sql = "INSERT INTO " + tableName + " ("
    columns=[]
    value=[]
    for k, v in values.items():
      columns.append(k)
      value.append(v)
    for c in columns:
      sql += "%s, " % c
    
    sql = sql[:-2]+") VALUES ("
    for v in value:
      sql += "%s, "
    sql = sql[:-2]+");"
    print(sql)
    self.cursor.execute(sql, tuple(value))
    self.db.commit()
    print("Element added to table {0}".format(tableName))
  
  def viewTable(self, tableName):
    sql = "SELECT * FROM " + tableName
    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    print(result)

newdb = Datab("creative_online_school_dot_com", "localhost", "root", "")
newdb.addTable("newTable", ID="int NOT NULL AUTO_INCREMENT PRIMARY KEY", First="varchar(40)", Last="varchar(40)")
newdb.addElement("newTable", First="David", Last="Baker")
newdb.addElement("newTable", First="creative", Last="school")
newdb.viewTable("newTable")
  