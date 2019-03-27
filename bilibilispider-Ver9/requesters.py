import requests
from proxies import get_proxy

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
	
def request_dom(url,headers=headers):
	'''请求url，返回dom文件'''
	try:
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response
		else:
			print('-'*30,'request doc error:',response.status_code)
	except requests.exceptions.ConnectionError:
		print('-'*30,'request doc ConnectionError')

################################################# 以下为up_msg_spider

def request_uploader_info(url,mid):
	'''请求up的个人信息和总体视频信息'''
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
		'Referer':'https://space.bilibili.com/{}/'.format(mid)}
	data = {'mid':mid,'csrf':''}
	try:
		response = requests.post(url,data=data,headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			print('-'*30,'request uploader_info error:',response.status_code)
	except requests.ConnectionError:
		print('-'*30,'request uploader_info ConnectionError')

def request_up_all_video(url,mid,headers=headers):
	'''根据mid请求up的总的视频信息'''
	data = {
	'mid':mid,
	'pagesize':30,
	'tid':0,
	'page':1,
	'keyword':'',
	'order':'pubdate'}
	try:
		response = requests.get(url,headers=headers,params=data)
		if response.status_code == 200:
			return response.json()
		else:
			print('-'*30,'request up_all_video error:',response.status_code)
	except requests.ConnectionError:
		print('-'*30,'request up_all_video ConnectionError')		

################################################# 以下为up_video_msg_spider

def request_each_page_video_info(url,mid,page,headers=headers):
	'''请求某页的视频信息'''
	data = {
	'mid':mid,
	'pagesize':30,
	'tid':0,
	'page':page,
	'keyword':'',
	'order':'pubdate'}
	try:
		response = requests.get(url,headers=headers,params=data)
		if response.status_code == 200:
			return response.json()
		else:
			print('-'*30,'request each_page_video_info error:',response.status_code)
	except requests.exceptions.ConnectionError:
		print('-'*30,'request each_page_video_info ConnectionError')







