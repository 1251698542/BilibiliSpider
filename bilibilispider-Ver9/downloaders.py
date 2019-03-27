'''
提供存储手段(mongo,json和csv)
'''
import re
import csv
import json
import pymongo

from config import *

client = pymongo.MongoClient(host=MONGO_URL)
db = client[MONGO_DB]

def return_vaild_name(title):
	'''标题合法化'''
	result = re.sub(r'[\\/:*?"<>|\r\n]+','_',title)
	return result


def save_to_csv(data,file_dir,file_name):
	file_name = return_vaild_name(file_name)
	file_url = 'download\\{}\\{}.csv'.format(file_dir,file_name)
	with open(file_url,'a',newline='',encoding='utf-8')as csvfile:
		fieldnames = [each for each in data.keys()]
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		# writer.writeheader()
		writer.writerow(data)
		print('数据已存储到:download\\{}\\{}.csv'.format(file_dir,file_name))

def save_to_json(data,file_dir,file_name):
	file_name = return_vaild_name(file_name)
	file_url = 'download\\{}\\{}.json'.format(file_dir,file_name)
	with open(file_url,'a',encoding='utf-8') as file:
		json.dump(data,file,ensure_ascii=False)
		file.write('\n')
		print('数据已存储到:download\\{}\\{}.json'.format(file_dir,file_name))

def save_to_jpg(data,file_dir,file_name):
	file_name = return_vaild_name(file_name)
	file_url = 'download\\{}\\{}.jpg'.format(file_dir,file_name)
	with open(file_url,'wb') as f:
		if f.write(data):	
			print('图片已存储到:download\\{}\\{}.jpg'.format(file_dir,file_name))
		else:
			print('--------图片存储失败:',file_name)

def save_to_mongo(table,data):
	if table.insert_one(data):
		print('数据已存储到mongodb:',data['name'])
	else:
		print('--------数据存储到mongodb失败:',data['name'])






def save_reply_to_json(data,file_dir,file_name):
	'''因为评论是以每层楼形式返回，若有print则打印太多，以此特供'''
	file_name = return_vaild_name(file_name)
	file_url = 'download\\{}\\{}.json'.format(file_dir,file_name)
	with open(file_url,'a',encoding='utf-8') as file:
		json.dump(data,file,ensure_ascii=False)
		file.write('\n')

def save_reply_to_csv(data,file_dir,file_name):
	file_name = return_vaild_name(file_name)
	file_url = 'download\\{}\\{}.csv'.format(file_dir,file_name)
	with open(file_url,'a',newline='',encoding='utf-8')as csvfile:
		fieldnames = [each for each in data.keys()]
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		# writer.writeheader()
		writer.writerow(data)
		
	

if __name__ == '__main__':
	uploader_info = {'name':'LexBurner','uid':777536,'sex':'男','level':6, 'regtime':1360404981,
			'describe':'bilibili 知名UP主、高能联盟成员', 'suffix':'代表作Lex吐槽系列',
			'sign':'新浪微博：http://weibo.com/lexburner',
			'img':'http://i0.hdslb.com/bfs/face/2996e22a24eed2d7767e452627a9130207defe6a.jpg',
			'birthday':'11-22','pages': 9,'视频总数':259,'动画':124,'游戏': 106,
			'科技': 1,'生活': 19,'国创':5,'影视':4}

	video_info= {'name':'【Lex】教练，我想打篮球，我想为所欲为','aid':16348266,'length':'23:08',
				'favorites':1543, 'comment':2272,
				'description':'相关游戏: 青春篮球\n简介补充: 会扣篮和抢板真的是能为所欲为'}

	# save_to_csv(uploader_info,UPLOADER_INFO_CSV_FILE_NAME)
	# save_to_mongo(db['777536'],video_info)

	# save_to_csv(video_info,777536)
	# save_to_mongo(db[UPLOADER_INFO_MONGO_TABLE_NAME],uploader_info)

