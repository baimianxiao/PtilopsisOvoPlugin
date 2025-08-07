# -*- encoding:utf-8 -*-

from .util import *

import sqlite3


# 数据库路径
user_sqlite_path = join(data_dir, "user_data.db")


def blacklist_sqlite_init(sqlite_path):
    conn = sqlite3.connect(sqlite_path)
    print("数据库打开成功")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);"""
    )
    print("黑名单数据表创建成功")
    conn.commit()
    conn.close()


def user_data_sqlite_init(sqlite_path):
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE USERDATA
           (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
           Name          TEXT    NOT NULL,
           QQ            TEXT     NOT NULL,   
           Ex            INT     NOT NULL,
           Level         INT     NOT NULL,
           Hcy           INT     NOT NULL,
           Time          char(50)
             );"""
    )
    cur.execute(
        "INSERT INTO USERDATA (ID,Name,QQ,Ex,Level,Hcy,Time) \
                          VALUES (1,'白咕咕', '2432115441',99999, 99999, 9999999,'2019/10/6' )"
    )
    conn.commit()
    conn.close()


# 黑名单数据操作
class BlacklistHandle:
    def __init__(self, sqlite_path: str):
        self.conn = sqlite3.connect(sqlite_path)
        self.cur = self.conn.cursor()
        print("已链接数据库")

    # 更新用户数据
    def user_data_insert(self, Name, QQ, Ex, Level, Hcy, Time):
        if self.user_data_select(QQ) is None:
            self.cur.execute(
                f"INSERT INTO BLACKLIST (Name,QQ,Ex,Level,Hcy,Time) \
                      VALUES ('{Name}',{QQ},{Ex},{Level},{Hcy},'{Time}' )"
            )
            self.conn.commit()
            return True
        else:
            return False

    # 检索用户数据
    def user_data_select(self, QQ):
        cursor = self.cur.execute(f"SELECT * from USERDATA WHERE QQ={QQ}")
        self.conn.commit()
        result = cursor.fetchall()
        if not result:
            return None
        return result

    # 更新用户数据
    def user_data_update(self, Name, QQ, Ex, Level, Hcy, Time):
        if self.user_data_select(QQ) is not None:
            self.cur.execute(
                f"UPDATE USERDATA set Name='{Name}',Ex={Ex},Level={Level},Hcy={Hcy},Time= '{Time}' where QQ={QQ}"
            )
            self.conn.commit()
            return True
        else:
            return False

    def user_data_delete(self, QQ):
        try:
            self.cur.execute(f"DELETE from USERDATA where QQ={QQ};")
            self.conn.commit()
            return True
        except:
            return False


# 用户数据操作
class UserDataHandle:
    def __init__(self, sqlite_path: str):
        self.conn = sqlite3.connect(sqlite_path)
        self.cur = self.conn.cursor()
        print("已链接数据库")

    # 更新用户数据
    def user_data_insert(self, Name, QQ, Ex, Level, Hcy, Time):
        if self.user_data_select(QQ) is None:
            self.cur.execute(
                f"INSERT INTO USERDATA (Name,QQ,Ex,Level,Hcy,Time) \
                      VALUES ('{Name}','{QQ}',{Ex},{Level},{Hcy},'{Time}' )"
            )
            self.conn.commit()
            return True
        else:
            return False

    # 检索用户数据
    def user_data_select(self, QQ):
        cursor = self.cur.execute(f"SELECT * from USERDATA WHERE QQ='{QQ}'")
        self.conn.commit()
        result = cursor.fetchall()
        if not result:
            return None
        return result

    # 更新用户数据
    def user_data_update(self, QQ, Ex, Level, Hcy, Time, Name=""):
        if self.user_data_select(QQ) is not None:
            if Name == "":
                self.cur.execute(
                    f"UPDATE USERDATA set  Ex={Ex},Level={Level},Hcy={Hcy},Time= '{Time}' where QQ='{QQ}'"
                )
                self.conn.commit()
                return True
            else:
                self.cur.execute(
                    f"UPDATE USERDATA set Name='{Name}', Ex={Ex},Level={Level},Hcy={Hcy},Time= '{Time}' where QQ='{QQ}'"
                )
                self.conn.commit()
                return True
        else:
            return False

    def user_data_delete(self, QQ):
        try:
            self.cur.execute(f"DELETE from USERDATA where QQ='{QQ}';")
            self.conn.commit()
            return True
        except:
            return False
