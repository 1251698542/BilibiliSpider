'''
整合模块
'''
from spiders import *
from config import *
 

def main():
	# 是使用up主昵称还是uid
	if USE_NAME:
		name_or_mid = Uploader_NameToUid_Spider(UPLOADER_NAME).crawl()
	else:
		name_or_mid = MID

	page,uploader_name = Uploader_Spider(name_or_mid).crawl()
	# 是否爬取每个视频的详细信息
	if CRAWL_ALL_VIDEO_INFO:
		Video_Spider(name_or_mid,uploader_name,page).crawl()


if __name__ == '__main__':
	main()