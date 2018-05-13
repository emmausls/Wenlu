# coding:utf-8

### MYSQL ###
'''
import MySQLdb

mysql = {
        'host':'localhost',
        'port':3306,
        'user':'root',
        'passwd':'',
        'database':'rp',
        }

def mysql_query(query):
    try:
        con = MySQLdb.connect(host = mysql['host'], user=mysql['user'],passwd=mysql['passwd'],db=mysql['database'],port=mysql['port'])
        cur=con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
        return rows

    except Exception as e:
 #       con.close()
        return str(e)


def mysql_exec(query):
    try:
        con = MySQLdb.connect(host = mysql['host'], user=mysql['user'],passwd=mysql['passwd'],db=mysql['database'],port=mysql['port'])
        cur=con.cursor()

        cur.execute(query)
        con.commit()
        con.close()
        return 0
    except Exception as e:
 #       con.close()
        return str(e)
'''
### POSTGRESQL ###
'''
import psycopg2

postgresql = {
    'host': '192.168.1.139',
    'port': 5432,
    'user': 'postgres',
    'passwd': '111111',
    'database': 'ifdoo',
}


def psql_query(query):
    try:
        con = psycopg2.connect(host=postgresql['host'], user=postgresql['user'], password=postgresql['passwd'],
                               database=postgresql['database'], port=postgresql['port'])
        cur = con.cursor()

        cur.execute(query)
        rows = cur.fetchall()
        return rows

    except Exception as e:
        #       con.close()
        return str(e)


def psql_exec(query):
    try:
        con = psycopg2.connect(host=postgresql['host'], user=postgresql['user'], password=postgresql['passwd'],
                               database=postgresql['database'], port=postgresql['port'])
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        return 0
    except Exception as e:
        #       con.close()
        return str(e)

'''
