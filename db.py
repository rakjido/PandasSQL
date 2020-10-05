
import pymysql
import pandas as pd 
import xml.etree.ElementTree as elemTree 

# from utils import _logger_set

# logger = _logger_set()

class db:
    @classmethod
    def connect(cls):
        tree = elemTree.parse('./config.xml')
        root = tree.getroot()
        dbinfo = root.find('./DATABASE')

        host = dbinfo.find('./host').text
        port = int(dbinfo.find('./port').text)
        userid = dbinfo.find('./userid').text
        password = dbinfo.find('./password').text
        db = dbinfo.find('./db').text

        try: 
            conn = pymysql.connect(host=host, port=port, user=userid, 
                                password=password, db=db, charset='utf8',
                                autocommit=True, cursorclass=pymysql.cursors.DictCursor )
        except BaseException:
            print("DB connection Error")

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        return conn, cursor

    @classmethod
    def select(cls, query, arg=None):
        conn, cursor = cls.connect()
        try :
            cursor.execute(query, arg)
            result = pd.DataFrame(cursor.fetchall())
        except Exception as e:
            print(e)            
        finally:
            conn.close()
        return result

    @classmethod
    def insert(cls, query, arg=None):
        conn, cursor = cls.connect()
        try :
            cursor.execute(query, arg)
            # autocommit = True
            # conn.commit()
        except Exception as e:
            print(e)
        finally:            
            conn.close()

    @classmethod
    def update(cls, query, arg=None):
        conn, cursor = cls.connect()
        try:
            cursor.execute(query, arg)
        except Exception as e:
            print(e)
        finally:            
            conn.close()
    
    @classmethod
    def delete(cls, query, arg=None):
        conn, cursor = cls.connect()
        try:
            cursor.execute(query, arg)
        except Exception as e:
            print(e)
        finally:            
            conn.close()
