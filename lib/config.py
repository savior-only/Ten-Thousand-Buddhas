# lib/config.py

#目标路径
target_path = 'target.txt'

#fofa配置
Fofa_API = 'https://fofa.info/api/v1/search/all?'
Fofa_API_email = ''
Fofa_API_KEY = ''
Fofa_logs = 'logs/fofa.log'

# TTBS数据库位置
result_sql_path = './results/result.sqlite3'

# wafw00f位置
wafw00f_path = './tools/wafw00f/wafw00f/main.py'

# crawlergo位置
crawlergo_path = './tools/crawlergo/crawlergo'
# chrome位置（有空格记得转义，放在tools目录最好）
chrome_path = "./tools/chrome/chrome"
# 爬虫同时开启最大标签页，即同时爬取的页面数量。
max_tab_count = "20"
# 发送爬虫结果到监听地址时的最大并发数
max_send_count = "10"
#传送到xray被动代理地址
push_to_proxy = "http://127.0.0.1:7777"

#xray位置
xray_path = './tools/xray/xray'
#Xray被动代理地址
xray_proxy = "127.0.0.1:7777"
#xray输出位置
xray_html = "logs/xray/xray.html"

# webhook
webhook_host='127.0.0.1'
webhook_port = '5000'
webhook = 'http://127.0.0.1:5000/webhook'
# 主页默认每页显示数目
PER_PAGE = 10


# Server酱SCKEY (http://sc.ftqq.com/?c=code)
sckey = "https://sctapi.ftqq.com/{你的key}.send"
