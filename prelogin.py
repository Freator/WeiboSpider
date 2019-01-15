# -*- coding:utf-8 -*-
import requests
import time
def get_server_data(su):
	# 构建URL
	prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)&_=%s' %(su,str(int(time.time() * 1000)))
	pre_data_res = session.get(prelogin_url, headers = headers, proxies = proxies)
	# 讲响应的内容转换为字典格式
	server_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))
	
	# #############################
	print(server_data)
	
	return server_data
if __name__ == "__main__":
	# 构造请求头
	agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
	headers = {'User-Agent': agent}
	# 代理IP，防止同一个IP登录多个不同微博账号
	proxies = {}
	# 新建会话
	session = requests.session()
	# 用户账号
	su = "186748014"
	server_data = get_server_data(su)