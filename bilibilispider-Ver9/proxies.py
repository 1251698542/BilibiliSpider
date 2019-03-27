'''
提供代理API
'''
import json
import random
# from spiders import Proxy_Spider

class Get_Proxy:
	def __init__(self):
		# proxy_spider = Proxies_Spider(40)
		# proxy_spider.crawl()
		
		fileurl = 'download\proxies_info\proxies.json'
		with open(fileurl,'r+')as file:
			self.proxies_list = [json.loads(line) for line in file.readlines()]
	def __call__(self):
		proxy = random.choice(self.proxies_list)
		return {'http':'http://{}:{}'.format(proxy['ip'],proxy['port'])}

get_proxy = Get_Proxy()

if __name__ == "__main__":
	x = get_proxy()
	print(x)
	print(type(x))
