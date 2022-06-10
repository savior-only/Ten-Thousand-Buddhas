# lib/sql_connect.py

import time
import sqlite3
from lib import config
from rich.console import Console

console = Console()

conn = sqlite3.connect(config.result_sql_path)

# 任务数据表检查
def task_sql_check():
    c = conn.cursor()
    console.print('正在检查任务数据表是否存在，如不存在则自动新建', style="#ADFF2F")
    try:
        c.execute('''CREATE TABLE TASK
            (ID INTEGER PRIMARY KEY ,
            URL             TEXT    NOT NULL,
            BANNER          TEXT    ,
            WAF             TEXT    ,
            STATUS          TEXT    ,
            TASK_TIME       TEXT    );
            ''')
        conn.commit()
    except:
        console.print('任务数据表已经存在', style="bold red")

#子域名数据表检查
def subdomain_sql_check():
    c = conn.cursor()
    console.print('正在检查子域名数据表是否存在，如不存在则自动新建', style="#ADFF2F")
    try:
        c.execute('''CREATE TABLE SUBDOMAIN
            (ID INTEGER PRIMARY KEY ,
            URL            TEXT     NOT NULL,
            SUBDOMAIN_TIME      TEXT    );
            ''')
        conn.commit()
    except:
        console.print('子域名数据表已经存在', style="bold red")

#漏洞数据表检查
def vuln_sql_check():
    c = conn.cursor()
    console.print('正在检查漏洞数据表是否存在，如不存在则自动新建', style="#ADFF2F")
    try:
        c.execute('''CREATE TABLE VULN
            (ID INTEGER PRIMARY KEY ,
            URL             TEXT    NOT NULL,
            PLUGIN          TEXT    ,
            VULN_TIME       TEXT    );
            ''')
        conn.commit()
    except:
        console.print('漏洞数据表已存在', style="bold red")

#插入SUBDOMAIN数据库
def insert_subdomain_sql(url_list):
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    console.print('TTBS数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    for url in url_list:
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            subdomain_c.execute("INSERT INTO SUBDOMAIN (URL, SUBDOMAIN_TIME) VALUES ('%s', '%s')"%(url, now_time))
            subdomain_conn.commit()
        except Exception as e:
            console.print('插入子域名数据库失败', url, style="bold red")
    console.print('插入子域名数据库成功',style="#ADFF2F")
    subdomain_conn.close()

# 读取SUBDOMAIN数据库
def read_subdomain_sql():
    subdomain_conn = sqlite3.connect(config.result_sql_path)
    console.print('TTBS数据库连接成功', style="#ADFF2F")
    subdomain_c = subdomain_conn.cursor()
    try:
        subdomains = subdomain_c.execute("select * from SUBDOMAIN").fetchall()
        return subdomains
    except:
        console.print('读取子域名数据库失败', style="bold red")
    console.print('读取子域名数据库成功', style="#ADFF2F")
    subdomain_conn.close()

# 插入TASK数据库
def insert_task_sql(url_list):
    task_conn = sqlite3.connect(config.result_sql_path)
    console.print('TTBS数据库连接成功', style="#ADFF2F")
    task_c = task_conn.cursor()
    for url in url_list:
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        try:
            task_c.execute("INSERT INTO TASK (URL,TASK_TIME) VALUES ('%s', '%s')"%(url,now_time))
            task_conn.commit()
        except Exception as e:
            print(e)
            console.print('插入数据库失败', url, style="bold red")
    console.print('插入任务数据库成功', style="#ADFF2F")
    task_conn.close()

#读取TASK数据库
def read_task_sql():
    task_conn = sqlite3.connect(config.result_sql_path)
    console.print('TTBS数据库连接成功', style="#ADFF2F")
    task_c = task_conn.cursor()
    try:
        task = task_c.execute("select * from TASK").fetchall()
        return task
    except:
        console.print('读取任务数据库失败', style="#ADFF2F")
    console.print('读取任务数据库成功', style="#ADFF2F")
    task_conn.close()

#插入漏洞数据库
def insert_vuln_sql(vuln):
    vuln_conn = sqlite3.connect(config.result_sql_path)
    console.print('漏洞数据库连接成功', style="#ADFF2F")
    vuln_c = vuln_conn.cursor()
    url = vuln["target"]["url"]
    plugin = vuln["plugin"]
    create_time = str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    vuln_list = [url, plugin, create_time]
    quey = "INSERT INTO VULN (URL, PLUGIN, VULN_TIME) VALUES (?,?,?)"
    vuln_c.execute(quey, vuln_list)
    vuln_conn.commit()
    vuln_conn.close()
