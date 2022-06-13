# lib/server.py

from flask import Flask, request
from lib import config, sql_connect
import requests
import datetime
import logging


app = Flask(__name__)

def push_ftqq(content):
    try:
        resp = requests.post(config.sckey, data={"title": "TTBS漏洞提醒", "desp": content})
        print(resp)
    except:
        if resp.json()["errno"] !=0:
            raise ValueError("push ftqq failed, %s" % resp.text)

@app.route('/webhook', methods=['POST'])
def xray_webhook():
    data = request.json
    vuln = data["data"]

    if "ratio_progress" in vuln:
        return "ok"
    if "baseline/sensitive/server-error" in vuln:
        return "ok"
    content = """### xray发现了新漏洞
url: {url}
插件/漏洞: {plugin}
发现时间: {create_time}
请及时查看和处理!!!""".format(url=vuln["target"]["url"], plugin=vuln["plugin"], create_time=str(datetime.datetime.fromtimestamp(vuln["create_time"] / 1000)))
    #print(vuln["target"]["url"])

    try:
        push_ftqq(content)
        sql_connect.insert_vuln_sql(vuln)
    except Exception as e:
        logging.exception(e)
    return 'ok'

if __name__ == '__main__':
    app.debug=True
    app.run(config.webhook_host,config.webhook_port)
