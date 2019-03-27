# bilibilispider

 爬取[bilibili网站](https://www.bilibili.com/)up主所有个人信息和所有视频信息



## 一.Requirements依赖项

```
python3
database:mongodb
module:requests,pymongo,BeautifulSoup,PyQuery
```



## 二.Description描述

1. 根据用户id或用户昵称，爬取bilibili网站up主的个人信息和视频信息,并下载到本地。
   **由于B站用户搜索功能缺陷，昵称查找有可能出错**。
2. 本项目的主要逻辑在`spiders.py`中。
3. 由于B站的评论反扒取机制较强，遂使用代理。但是**不排除被BAN的可能**。如需关闭，前往`config.py`关闭。
   由于使用的是免费代理，代理时效较差。
   如需更新代理，前往`spiders.py`执行`Proxy_Spider`。
   如需检测网络和代理的通畅，前往`spiders.py`执行`Test_Spider`。
4. 支持存储三种格式(可多选):
  * json
  * csv
  * mongoDB



## 三.本项目爬取的信息

**个人信息**:

```
昵称,用户id,头像
性别,等级,生日,签名,自述
粉丝数,关注数,视频总播放数
代表作
宏观视频信息
```
**视频信息**:

```
标题,封面,视频id,av号
时长,视频简介,标签
硬币数,弹幕数,收藏数,评论数,分享数,观看数,是否原创
弹幕,评论
```



## 四.download文件夹:

```
proxies_info : 储存代理ip
uploaders_img ：储存up主的头像图片
uploaders_info ：储存up主的个人信息
video_bulletscreen_info : 储存视频的弹幕信息
video_img ：储存视频的封面
video_info ：储存up主的所有视频信息
video_reply_info ：储存视频评论（零评论则不会保存）
```



