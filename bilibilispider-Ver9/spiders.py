'''
up主昵称转mid爬虫，up主个人宏观信息爬虫，up主视频宏观信息爬虫，up主代表作爬虫，up主粉丝数爬虫
视频详细信息爬虫，弹幕爬虫，评论爬虫，标签爬虫，观看信息爬虫
测试爬虫，代理爬虫

Uploader_Spider为up主个人宏观信息爬虫，up主视频普通信息爬虫，up主代表作爬虫，up主粉丝数爬虫的整合
Video_Spider为视频详细信息爬虫，弹幕爬虫，评论爬虫，标签爬虫，观看信息爬虫的整合
'''
import sys
import json
from multiprocessing import Pool

from requesters import *
from parsers import *
from downloaders import *
from config import *

class Spider:
	def crawl(self):
		raise NotImplemented


class Uploader_Spider(Spider):
	'''爬取up主个人信息，API为mid'''
	def __init__(self,mid):		
		self.mid = mid
	def download_portrait(self,pic_url,pic_name):
		'''下载up主头像'''
		content = request_dom(pic_url).content
		if content:
			save_to_jpg(content,'uploaders_img',pic_name)
	def crawl(self):
		uploader_fans_spider = Uploader_Fans_Spider(self.mid)
		uploader_general_msg_spider = Uploader_General_Msg_Spider(self.mid)
		uploader_masterpiece_spider = Uploader_MasterPiece_Spider(self.mid)
		uploader_general_video_spider = Uploader_General_Video_Msg_Spider(self.mid)
		
		dict1 = uploader_fans_spider.crawl() if CRAWL_UPLOADERS_FANS_INFO else {}
		dict2 = uploader_general_msg_spider.crawl()
		dict3 = uploader_masterpiece_spider.crawl() if CRAWL_UPLOADERS_MASTERPIECE_INFO else {}
		dict4 = uploader_general_video_spider.crawl() 

		total_dict = dict(dict1,**dict2,**dict3,**dict4)

		# 是否下载up主头像
		if DOWMLOAD_PORTRAIT:
			uploader_name = total_dict['uid'] if UES_MID_AS_FILE_NAME else total_dict['name']
			self.download_portrait(total_dict['img'],uploader_name)

		# config控制输出
		# 如果爬取up主个人信息
		if CRAWL_UPLOADERS_INFO:  
			# 输出设置
			if not (SAVE_TO_MONGODB or SAVE_TO_CSV or SAVE_TO_JSON):   
				sys.stdout.write(str(total_dict) + '\n')
			else:
				if SAVE_TO_JSON:save_to_json(total_dict,'uploaders_info',UPLOADER_INFO_CSV_FILE_NAME)
				if SAVE_TO_CSV:save_to_csv(total_dict,'uploaders_info',UPLOADER_INFO_CSV_FILE_NAME)
				if SAVE_TO_MONGODB:save_to_mongo(db[UPLOADER_INFO_MONGO_TABLE_NAME],total_dict)
		# 返回up总共有多少页视频，up的昵称(这两个参数传给Video_Spider)
		return total_dict['pages'],total_dict['name']

class Video_Spider(Spider):
	'''爬取up主每个视频的详细信息，API为mid,uploader_name,page'''
	def __init__(self,mid,uploader_name,page):
		self.mid = mid
		self.uploader_name = uploader_name
		self.page = page
	def integration(self,page):
		'''完成某一页数据的“获取-解析-保存”流程'''
		# 数据库表的名称
		uploader_VideoInfo_table = db[str(self.mid)] if UES_MID_AS_FILE_NAME else db[self.uploader_name]

		video_detail_msg_spider = Video_Detail_Msg_Spider(self.mid,self.uploader_name,page)
		for each_video_dict in video_detail_msg_spider.crawl():

			av = each_video_dict['aid']                                         # 视频的av号
			video_name = av if UES_AV_AS_FILE_NAME else each_video_dict['name'] # 视频的title
			print('-'*10,'开始存储：av{}'.format(av))
						
			tag_spider = Tag_Spider(av)
			view_spider = View_Spider(av)

			dict1 = tag_spider.crawl()
			dict2 = view_spider.crawl()

			# 合并字典
			total_dict = dict(each_video_dict,**dict1,**dict2)
			print(total_dict)

			# 是否下载每部的视频弹幕
			if DOWMLOAD_VIDEO_BULLET:
				bulletscreen_spider = BulletScreen_Spider(av)
				bulletscreen = bulletscreen_spider.crawl()

				if SAVE_TO_JSON:save_to_json(bulletscreen,'video_bulletscreen_info',video_name)
			
			# 是否下载每部的视频评论
			if DOWMLOAD_VIDEO_REPLY:
				reply_spider = Reply_Spider(av)
				if SAVE_TO_CSV:
					for reply in reply_spider.crawl():
						save_reply_to_csv(reply,'video_reply_info',video_name)
					print('数据已存储到:download\\{}\\{}.csv'.format('video_reply_info',video_name))
				if SAVE_TO_JSON:
					for reply in reply_spider.crawl():
						save_reply_to_json(reply,'video_reply_info',video_name)
					print('数据已存储到:download\\{}\\{}.json'.format('video_reply_info',video_name))

			# 每部视频信息的存储设置
			if not (SAVE_TO_MONGODB or SAVE_TO_CSV or SAVE_TO_JSON):
				sys.stdout.write(str(total_dict) + '\n')
			else:
				# 确定保存文件的文件名
				file_name = str(self.mid) if UES_MID_AS_FILE_NAME else self.uploader_name
				if SAVE_TO_CSV:save_to_csv(total_dict,'video_info',file_name)
				if SAVE_TO_JSON:save_to_json(total_dict,'video_info',file_name)
				if SAVE_TO_MONGODB:save_to_mongo(uploader_VideoInfo_table,total_dict)
	def crawl(self):
		pool = Pool()
		pool.map(self.integration,range(1,self.page+1))
		pool.close()



class Uploader_NameToUid_Spider(Spider):
	'''根据up主的昵称转为uid'''
	def __init__(self,keyword):
		self.url = 'https://search.bilibili.com/upuser?keyword={}&single_column=0&user_type=0'.format(keyword)
	def crawl(self):
		response = request_dom(self.url).text
		if response:
			uploader_uid = parse_uploadernametouid(response)
			return uploader_uid

class Uploader_General_Video_Msg_Spider(Spider):
	'''获取up主宏观的视频信息'''
	def __init__(self,mid):
		self.mid = mid
	def crawl(self):
		self.url = 'https://space.bilibili.com/ajax/member/getSubmitVideos'
		video_info = request_up_all_video(self.url,self.mid)

		if video_info:
			video_info_dict = parse_up_all_video(video_info)
			return video_info_dict
		else:
			print('-'*30,'video_info 404')	
			return {}	

class Uploader_General_Msg_Spider(Spider):
	'''获取up主个人信息和总体视频信息的api(普通信息，如性别年龄)'''
	def __init__(self,mid):
		self.mid = mid
	def crawl(self):
		self.url = 'https://space.bilibili.com/ajax/member/GetInfo'
		uploader_info = request_uploader_info(self.url,self.mid)

		if uploader_info:
			uploader_info_dict = parse_uploader_info(uploader_info)
			return uploader_info_dict
		else:
			print('-'*30,'uploader_info 404')
			return {}

class Uploader_MasterPiece_Spider(Spider):
	'''up主代表作'''
	def __init__(self,mid):
		self.mid = mid
	def crawl(self):
		self.url = 'https://space.bilibili.com/ajax/masterpiece/get?mid={}&guest=1'.format(self.mid)
		response = request_dom(self.url).text
		if response and response.startswith(u'\ufeff'):
			response = json.loads(response.encode('utf-8')[3:].decode('utf8'))
			masterpiece = parse_masterpiece(response)
			return masterpiece
		else:
			print('-'*30,'MasterPiece 404')
			return {}

class Uploader_Fans_Spider(Spider):
	'''up主粉丝数和关注数'''
	def __init__(self,mid):
		self.mid = mid
	def crawl(self):
		self.url = 'https://api.bilibili.com/x/relation/stat?jsonp=jsonp&vmid={}'.format(self.mid)
		response = request_dom(self.url).json()

		if response:
			fans_dict = parse_fans_info(response)
			return fans_dict
		else:
			print('-'*30,'fans_dict 404')
			return {}



class Video_Detail_Msg_Spider(Spider):
	'''获取up主每一页视频的详细信息'''
	def __init__(self,mid,uploader_name,page):
		# up主概括的视频信息的api
		self.url = 'https://space.bilibili.com/ajax/member/getSubmitVideos'
		self.uploader_name = uploader_name
		self.mid = mid
		self.page = page
	def crawl(self):
		'''完成某一页数据的“获取-解析-保存”流程'''		
		video_info = request_each_page_video_info(self.url,self.mid,self.page)
		if video_info:
			for each_video in parse_each_page_video_info(video_info):
				yield each_video
			
class BulletScreen_Spider(Spider):
	'''抓取av的全部弹幕，API为av号'''
	def __init__(self,av):
		self.doc_url = 'https://www.bilibili.com/video/av{av}'.format(av=av)
	def crawl(self):
		doc = request_dom(self.doc_url).text
		if doc:
			cid = parse_doc_to_get_cid(doc)
			bullet_screen_url = 'https://comment.bilibili.com/{cid}.xml'.format(cid=cid)
			xml_file = request_dom(bullet_screen_url).content.decode('utf-8',"ignore")
			bulletscreen = parse_bulletscreen(xml_file)
			return bulletscreen

class Reply_Spider(Spider):
	'''抓取av的全部评论，API为av号'''
	def __init__(self,av):
		self.av = av
		self.url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={av}&sort=0'.format(av=self.av)
	def get_reply_page(self):
		'''获取总共几页评论'''
		response = request_dom(self.url).json()
		if response:
			count = response.get('data').get('page').get('count')    # 总共有几条评论
			page = int(count)//20 + 2                                # 总共有几页评论
			return page
		else:
			print('-'*30,'reply 404')
	def crawl(self):
		'''整合前面的函数'''
		page = self.get_reply_page()
		if page:
			for pn in range(1,page):
				url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={pn}&type=1&oid={av}&sort=0'.format(pn=pn,av=self.av)
				response = request_dom(url).json()
				if response:
					for each_floor in parse_reply(response):
						yield each_floor
				else:
					print('-'*30,'video reply 404')

class Tag_Spider(Spider):
	'''抓取av的标签，封面，标题，API为av号'''
	def __init__(self,av):
		self.av = av
		self.url = 'https://www.bilibili.com/video/av{}'.format(self.av)
	def crawl(self):
		html = request_dom(self.url).text
		if html:
			tags,pic_url,title = parse_tags(html)
			file_name = self.av if UES_AV_AS_FILE_NAME else title
			# 是否下载每部的视频封面(前提是必须开启下载每个的视频信息)
			if DOWMLOAD_VIDEO_COVER and pic_url:
				data = request_dom(pic_url).content
				save_to_jpg(data,'video_img',file_name)
			return {'tags':tags}
		return {}

class View_Spider(Spider):
	'''获取硬币数,弹幕数,收藏数,评论数,分享数,观看数,是否原创数，API为av号'''
	def __init__(self,av):
		self.url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(av)
	def crawl(self):
		json_file = request_dom(self.url).json()
		if json_file:
			msg_dict = parse_view_info(json_file)
			return msg_dict
		return {}



class Test_Spider(Spider):
	def __init__(self):
		self.url1 = 'https://www.bilibili.com'
		self.url2 = 'http://httpbin.org/get'
		self.max_count = 8
	def show(self,url,last_time,connect_count,response):
		print('*'*50)
		print('{:<15}: {}'.format('test url',url))

		if url == 'http://httpbin.org/get':
			import json
			response = json.loads(response)
			print('{:<15}: {}'.format('test ip',response['origin']))

		print('{:<15}: {:.2f}s'.format('length of time',last_time))
		print('{:<15}: {}'.format('connect count',connect_count))
		print('*'*50)
	def test(self,url):
		import time
		connect_count = 1
		first = time.perf_counter()
		while connect_count <= self.max_count:
			response = request_dom(url).text
			if response:
				last_time = time.perf_counter() - first
				print('successful:')
				self.show(url,last_time,connect_count,response)						
				return None
			connect_count += 1
		last_time = time.perf_counter() - first
		print('failed')
		self.show(url,last_time,self.max_count,response)
	def crawl(self):
		self.test(self.url1)
		self.test(self.url2)

class Proxy_Spider(Spider):
	def __init__(self,idx):
		self.idx = idx
	def crawl(self):
		for page in range(1,self.idx+1):
			self.url1 = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
			self.url2 = 'http://www.ip3366.net/?stype=1&page={}'.format(page)
			self.url3 = 'http://www.89ip.cn/index_{}.html'.format(page)
			
			html1 = request_dom(self.url1).text
			html2 = request_dom(self.url2).text
			html3 = request_dom(self.url3).text

			for each in parse_proxies(html1,1,2):
				save_to_json(each,'proxies_info','proxies')
			for each in parse_proxies(html2,1,2):
				save_to_json(each,'proxies_info','proxies')
			for each in parse_proxies(html2,1,2):
				save_to_json(each,'proxies_info','proxies')


if __name__ == '__main__':
	av = 36588386
	mid = 63231
	keyword = '泛式'
	# mid = 8776244

####################################################################################

	# # 根据up昵称转化为uid的爬虫
	# uploader_nametouid_spider = Uploader_NameToUid_Spider(keyword)
	# x = uploader_nametouid_spider.crawl()
	# print(x)

	# # up主个人信息爬虫
	# uploader_spider = Uploader_Spider(mid)
	# x = uploader_spider.crawl()
	# print(x)

	# # up主视频信息爬虫
	# video_spider = Video_Spider(mid,str(mid),1)
	# video_spider.crawl()

####################################################################################

	# # up主概括的视频信息爬虫
	# uploader_general_video_spider = Uploader_General_Video_Msg_Spider(63231)
	# x = uploader_general_video_spider.crawl()
	# print(x)

	# # up主普通个人信息爬虫
	# uploader_general_msg_spider = Uploader_General_Msg_Spider(mid)
	# x = uploader_general_msg_spider.crawl()
	# print(x)

	# # up主代表作爬虫
	# uploader_masterpiece_spider = Uploader_MasterPiece_Spider(mid)
	# x = uploader_masterpiece_spider.crawl()
	# print(x)

	# # up主粉丝数和关注数爬虫
	# uploader_fans_spider = Uploader_Fans_Spider(mid)
	# x = uploader_fans_spider.crawl()
	# print(x)

####################################################################################

	# # 每一页视频普通信息的爬虫
	# Video_Detail_Msg_Spider = Video_Detail_Msg_Spider(mid,str(mid),1)
	# for x in video_detail_msg_spider.crawl():
	# 	print(x)

	# # 弹幕爬虫
	# bulletscreen_spider = BulletScreen_Spider(av)
	# x = bulletscreen_spider.crawl()
	# print(x)

	# # 评论爬虫
	# reply_spider = Reply_Spider(av)
	# for each in reply_spider.crawl():
	# 	print(each)

	# # 标签、封面爬虫
	# tag_spider = Tag_Spider(4611873)
	# x = tag_spider.crawl()
	# print(x)

	# # 观看信息爬虫
	# view_spider = View_Spider(av)
	# x = view_spider.crawl()
	# print(x)

####################################################################################

	# 测试代理ip爬虫
	test_spider = Test_Spider()
	test_spider.crawl()

	# # 代理爬虫
	# proxy_spider = Proxy_Spider(40)
	# proxy_spider.crawl()
