import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

from config import *
################################################# 以下为up_msg_spider

def parse_uploader_info(json_file):
	'''解析出up的个人信息'''
	data = json_file.get('data')

	return{
	'name'    : data.get('name'),
	'uid'     : data.get('mid'),
	'sex'     : data.get('sex'),
	'level'   : data.get('level_info').get('current_level'),
	'regtime' : data.get('regtime'),
	'describe': data.get('official_verify').get('desc'),
	'suffix'  : data.get('official_verify').get('suffix'),
	'sign'    : data.get('sign').strip(),
	'img'     : data.get('face'),
	'birthday': data.get('birthday'),}

def parse_up_all_video(json_file):
	'''解析出up主总的视频信息'''
	data = json_file.get('data')
	tlist = data.get('tlist')

	sort = [each for each in tlist]
	anime   = tlist.get('1').get('count') if '1' in sort else 0,
	game    = tlist.get('4').get('count') if '4' in sort else 0,
	science = tlist.get('36').get('count') if '36' in sort else 0,
	live    = tlist.get('160').get('count') if '160' in sort else 0,
	china   = tlist.get('167').get('count') if '167' in sort else 0,
	movie   = tlist.get('181').get('count') if '181' in sort else 0,

	return {
	'pages':data.get('pages'),  # 显示在个人空间视频共有几页
	'视频总数':data.get('count'),
	'动画':anime[0],
	'游戏':game[0],
	'科技':science[0],
	'生活':live[0],
	'国创':china[0],
	'影视':movie[0],}

def parse_fans_info(json_file):
	'''解析出up主的粉丝信息'''
	data = json_file.get('data')

	following = data.get('following') # 关注者
	follower  = data.get('follower')  # 粉丝

	return {'following':following,'follower':follower}

################################################# 以下为up_video_msg_spider

def parse_each_page_video_info(json_file):
	'''解析某页的视频信息'''
	vlist = json_file.get('data').get('vlist')
	for each in vlist:
		title       = each.get('title').strip()
		aid         = each.get('aid')
		comment     = each.get('comment')
		description = each.get('description')
		favorites   = each.get('favorites')
		length      = each.get('length')

		if title:
			yield{
			'name': title,
			'aid': aid,
			'length': length,
			'favorites': favorites,
			'comment': comment,
			'description': description,}

################################################# 以下为bulletscreen_spider

def parse_doc_to_get_cid(doc):
	'''解析doc得到cid'''
	result = re.search(r'"cid":(\d+),"dimension"',doc,re.S)
	return result.group(1)

def parse_bulletscreen(xml_file):
	'''解析xml文件得到弹幕'''
	soup = BeautifulSoup(xml_file,'lxml')
	# 弹幕去重
	if BULLETSCREEN_IS_DISTINCT:
		result = list(set([each.text for each in soup.select('d')]))
	else:
		result = [each.text for each in soup.select('d')]
	return result

################################################# 以下为reply_spider

def parse_reply(data):
	'''抓取一页(20条)评论'''
	replies = data.get('data').get('replies')

	for each_reply in replies:
		member = each_reply.get('member')  
		yield {
		'floor'       : each_reply.get('floor'),                           # 评论层数
		'message'     : each_reply.get('content').get('message').strip(),  # 评论内容		
		'like'        : each_reply.get('like'),                            # 评论赞数
		'member_mid'  : member.get('mid'),                                 # 评论人uid
		'member_name' : member.get('uname'),                               # 评论人昵称
		'menber_level': member.get('level_info').get('current_level'),     # 评论人等级
		'member_sex'  : member.get('sex'),                                 # 评论人性别
		'member_sign' : member.get('sign').strip(),                        # 评论人签名
		'member_img'  : member.get('avatar'),                              # 评论人头像链接
		}

################################################# 以下为video_tag_spider

def parse_tags(html):
	doc = pq(html)

	pic_url = doc('meta[itemprop="image"]').attr('content')
	title = doc('h1 span').text()
	tags = re.findall(r'"tag_name":"(.*?)"',html,re.S)
	return tags,pic_url,title

################################################# 以下为video_view_spider

def parse_view_info(data):
	'''解析得出视频的观看信息'''
	msg = data.get('data')

	return {
	'av'           : msg.get('aid'),
	'coin'         : msg.get('coin'),      # 硬币
	'bullet_screen': msg.get('danmaku'),   # 弹幕
	'favorite'     : msg.get('favorite'),  # 收藏
	'reply'        : msg.get('reply'),     # 评论
	'share'        : msg.get('share'),     # 分享
	'view'         : msg.get('view'),      # 观看
	'copyright'    : msg.get('copyright'), # 是否原创，原创为1,非原创为2
	}
################################################# 以下为MasterPiece_Spider

def parse_masterpiece(json_file):
	data = json_file.get('data')
	if data:
		return {'masterpiece':data}
	return {'masterpiece':None}

################################################# 以下为proxies_spider

def parse_proxies(html,ip_child,port_child):
    '''从html中解析出包含的代理信息'''
    if html:
        tr_tags = pq(html)('tr').items()
        for tr_tag in tr_tags:
            ip   = tr_tag('td:nth-child({})'.format(ip_child)).text()
            port = tr_tag('td:nth-child({})'.format(port_child)).text()
            if ip:
                yield {'ip':ip,'port':port}
    else:print('-'*30,'html不存在')

################################################# 以下为Uploader_MameToUid_Spider

def parse_uploadernametouid(html):
	mid = re.search(r'space\.bilibili\.com/(.*?)\?from',html,re.S)
	if mid:
		return mid.group(1)
	return '查无此人'
