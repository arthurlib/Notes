```python
import contextlib

import pymysql

config = {
    'host': "",
    'port': "",
    'user': "",
    'password': "",
    'database': "",
    'charset': "",
}


def get_dev_db():
    return DB(host="192.168.18.168",
              port=3306,
              user="root",
              password="s4sipoaA",
              database="s4s")


@contextlib.contextmanager
def get_conn(config):
    conn = None
    try:
        conn = pymysql.connect(**config)
        yield conn
    finally:
        if conn:
            conn.close()


class DB(object):
    def __init__(self, host=None, port=None, user=None, password=None, database=None, charset='utf8'):
        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cursor = self.db.cursor()

    def query_with_ping(self, sql):
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_with_ping(self, sql):
        """会在操作之前先ping一下重连"""
        self.db.ping(reconnect=True)
        self.cursor.execute(sql)
        self.db.commit()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def get_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_all_with_dict(self, sql):
        rows = self.query(sql)
        names = [d[0] for d in self.cursor.description]
        data = [dict(zip(names, row)) for row in rows]
        return data

    def get_one_with_dict(self, sql):
        row = self.get_one(sql)
        names = [d[0] for d in self.cursor.description]
        data = dict(zip(names, row))
        return data
```
