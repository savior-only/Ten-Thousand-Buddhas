#python3
#___utf-8___

import sys
import time
import os
from rich.console import Console
from rich.table import Column, Table
from lib.read_target import read_target
from lib import config, fofa, subdomain_collect, waf_check, sql_connect, craw_to_xray

console = Console()

# banner生成函数
def banner():
    msg = '''
                                          _                                  
                                       _ooOoo_                               
                                      o8888888o                              
                                      88" . "88                              
                                      (| -_- |)                              
                                      O\  =  /O                              
                                   ____/`---'\____                           
                                 .'  \\|     |//  `.                         
                                /  \\|||  :  |||//  \                        
                               /  _||||| -:- |||||_  \                       
                               |   | \\\  -  /'| |   |                       
                               | \_|  `\`---'//  |_/ |                       
                               \  .-\__ `-. -'__/-.  /                       
                             ___`. .'  /--.--\  `. .'___                     
                          ."" '<  `.___\_<|>_/___.' _> \"".                  
                         | | :  `- \`. ;`. _/; .'/ /  .' ; |    Buddhas       
                         \  \ `-.   \_\_`. _.'_/_/  -' _.' /                 
           ================-.`___`-.__\ \___  /__.-'_.'_.-'================  
                                       `=--=-'                    bxc        
    '''

    console.print(msg, style="bold yellow")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ABOUT", style="dim", width=35)
    table.add_column("AUTHOR", style="dim", width=35)
    table.add_column("PLUGINS", style="dim", width=35)
    help_table = Table(show_header=True, header_style="bold magenta")
    help_table.add_column("ID", style="dim", width=35)
    help_table.add_column("参数", style="dim", width=35)
    help_table.add_column("说明", style="dim", width=35)
    table.add_row(
        "一款互联网暴露面资产快速打点工具",
        "Abai",
        "Fofa"
    )
    table.add_row(
        "",
        "",
        "Wafw00f"
    )
    table.add_row(
        "",
        "",
        "Crawlergo"
    )
    table.add_row(
        "",
        "",
        "Xray"
    )
    help_table.add_row(
        "1",
        "Fofa_collect",
        "获取子域名"
    )
    help_table.add_row(
        "2",
        "Waf_Check",
        "WAF检测"
    )
    help_table.add_row(
        "3",
        "Craw_To_Xray",
        "爬虫爬取 + 漏洞探测 + 消息通知"
    )
    help_table.add_row(
        "4",
        "View",
        "查看"
    )
    help_table.add_row(
        "5",
        "Exit",
        "退出"
    )
    console.print(table)
    console.print('参数说明', style="#ADFF2F")
    console.print(help_table)

#结束函数
def end():
    console.print("shutting down at {}".format(time.strftime("%X")), style="#ADFF2F")

def main():
    banner()
    while True:
        console.print('请输入要执行的参数ID: [bold cyan]1-5[/bold cyan]', style="#ADFF2F")
        args = input('> ')
        if args == '1':
            fofa.Fofa_collect(read_target(config.target_path)) # fofa获取子域名
        elif args == '2':
            waf_check.waf_check(sql_connect.read_task_sql())
        elif args == '3':
            craw_to_xray.craw_to_xray(sql_connect.read_task_sql())
        elif args == '4':
            run_html.main()
        elif args == '5':
            server_cmd = 'mv ./results/result.sqlite3 ./results/{}.sqlite3'.format(time.strftime("%Y_%m_%d_%H_%M_%S"))
            stop_server_cmd = "ps -ef |grep server.py |awk '{print $2}'|xargs kill -9"
            stop_xray_cmd = "ps -ef |grep xray |awk '{print $2}'|xargs kill -9"
            os.system(server_cmd)
            os.system(stop_server_cmd)
            os.system(stop_xray_cmd)
            console.print('server及xray服务已停止\n数据库已根据当前时间戳重命名{}.sqlite3'.format(time.strftime("%Y_%m_%d_%H_%M_%S")), style="#ADFF2F")
            break
        else:
            console.print('输入参数有误，请检查后输入', style="#ADFF2F")
            sys.exit()
    end()


if __name__ == '__main__':
    main()
