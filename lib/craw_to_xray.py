# lib/craw_to_xray.py

import sqlite3
import subprocess
from lib import config
from rich.console import Console

console = Console()

#爬虫爬去且发送到XRAY

def craw_to_xray(domain_list):
    console.print('正在进行爬虫探测+漏洞探测', style="#ADFF2F")
    server_cmd = 'nohup python3 server.py > logs/server.log 2>&1 &'
    subprocess.Popen(server_cmd, shell=True)
    xray_cmd = 'nohup ' + config.xray_path + ' webscan --listen ' + config.xray_proxy + ' --html-output ' + config.xray_html +  ' --webhook-output ' + config.webhook + ' > logs/xray.log 2>&1 &'
    subprocess.Popen(xray_cmd, shell=True)
    console.print('任务数据库连接成功',style="#ADFF2F")
    conn = sqlite3.connect(config.result_sql_path)
    c = conn.cursor()
    for domain in domain_list:
        domain =domain[1]
        cmd = config.crawlergo_path + " -c " + config.chrome_path + " -t " + config.max_tab_count + " -f " + " smart " + " --fuzz-path " + " --push-to-proxy " + config.push_to_proxy + " --push-pool-max " + config.max_send_count + " " + domain
        console.print('即将开启爬虫模块，可通过[bold cyan]tail -f logs/xray.log[bold cyan]查看进度信息', style="#ADFF2F")
        rsp = subprocess.Popen(cmd, shell=True)
        while True:
            if rsp.poll() == None:
                pass
            else:
                break
