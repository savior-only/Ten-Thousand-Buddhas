# lib/fofa.py

import requests
import base64
import json
from lib import config, sql_connect
from rich.console import Console

console = Console()

def Fofa_collect(target):
    url_list = []

    for i in target:
        search = 'domain="{}"'.format(i)
        console.print('正在使用fofa搜集子域名：', i, style="#ADFF2F")
        query = base64.b64encode(search.encode('utf-8'))    # 对查询语法进行base64加密
        fquery=str(query,"utf-8")   # 获取值
        api = config.Fofa_API + 'email=' + config.Fofa_API_email + '&key=' + config.Fofa_API_KEY + '&qbase64={}&page=1&size=10000'.format(fquery)
        #print(api)

        try:
            response = requests.get(api)
            res = json.loads((response.content).decode('utf-8'))

            # 对results结果取值进行for循环
            for i in range(len(res["results"])):
                url = res["results"][i][0] # 循环读取url
                if url[:4] != 'http': # 通过前4个字符判断是否为完整的url链接
                    url = 'http://' + url
                url_list.append(url.strip())
            
        except Exception as e:
            print(e)
            console.print('fofa查询异常，请检查配置是否正确', style="bold red")
            return url_list
    console.log('子域收集完成')
    sql_connect.task_sql_check()
    sql_connect.subdomain_sql_check()
    sql_connect.vuln_sql_check()
    sql_connect.insert_subdomain_sql(url_list)
    sql_connect.insert_task_sql(url_list)


        