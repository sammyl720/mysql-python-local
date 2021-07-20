#!/usr/bin/python

import pymysql
htmlString=''

def headHTML(htmlString):
    htmlString+='<!DOCTYPE html>\n'
    htmlString+='<html lang="en">\n'
    htmlString+='<head>\n'
    htmlString+='<title>\n'
    htmlString+='Owners of Pets\n'
    htmlString+='</title>\n'
    htmlString+='</head>\n'
    htmlString+='<body>\n'
    return htmlString

def footHTML(htmlString):
    htmlString+='</body>\n'
    htmlString+='</html>\n'
    return htmlString

def ownerQuery():
    db = pymysql.connect(host='localhost', user='root', passwd='', db='creative_online_school')
    cursor=db.cursor()
    sql = 'SELECT * FROM owners;'
    cursor.execute(sql)
    owners = cursor.fetchall()
    sql = 'SELECT column_name from information_schema.COLUMNS where TABLE_NAME=' + "'owners';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    print(columns)
    return(owners,columns)

def ownersTable(owners_list,column_names,html):
    html += '<table border="1">\n'
    html += '<tr>\n'
    i=0
    for column in column_names:
        html += '<th>' + column[0] + '</th>\n'
        i+=1
    html += '</tr>\n'
    for owner in owners_list:
        html += '<tr>\n'
        r=0
        while r<i:
            html += '<td>{0}</td>'.format(owner[r])
            r+=1
        html += '\n</tr>\n'
    html += '</table>\n'
    return html

def petsTable(pets_list,column_names,html):
    html += '<table border="1">\n'
    html += '<tr>\n'
    i=0
    for column in column_names:
        html += '<th>' + column[0] + '</th>='
        i+=1
    html += '\n</tr>\n'
    for pet in pets_list:
        html += '<tr>\n'
        r=0
        while r<i:
            html += '<td>{0}</td>'.format(pet[r])
            r+=1
        html += '</tr>\n'
    html += '</table>\n'
    return html
def petquery():
  db = pymysql.connect(host='localhost', user='root', passwd='', db='creative_online_school')
  cursor=db.cursor()
  sql = 'SELECT * FROM pets;'
  cursor.execute(sql)
  pets = cursor.fetchall()
  sql = 'SELECT column_name from information_schema.COLUMNS where TABLE_NAME=' + "'pets';"
  cursor.execute(sql)
  columns = cursor.fetchall()
  print(columns)
  return(pets,columns)

if __name__=='__main__':
    htmlString=headHTML(htmlString)
    (owners,headers) = ownerQuery()
    htmlString=ownersTable(owners,headers,htmlString)
    (pets, headers) = petquery()
    htmlString=petsTable(pets,headers,htmlString)
    htmlString=footHTML(htmlString)
    outf = open('render.html','w')
    outf.write(htmlString)
    outf.close()
