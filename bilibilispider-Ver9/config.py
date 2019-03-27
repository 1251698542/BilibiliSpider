#####################################################################  以下为爬取设置

# 是否下载up主头像
DOWMLOAD_PORTRAIT = True

# 是否爬取up主的个人信息(如是false则以下的爬取设置失效)
CRAWL_UPLOADERS_INFO = True

# 是否爬取up主代表作的视频信息
CRAWL_UPLOADERS_MASTERPIECE_INFO = True

# 是否爬取up主的粉丝信息
CRAWL_UPLOADERS_FANS_INFO = True



# 是否爬取up主的每个视频的详细信息(如是false则以下的爬取设置失效)
CRAWL_ALL_VIDEO_INFO = True

# 是否下载每个视频的封面
DOWMLOAD_VIDEO_COVER = True

# 是否下载每个视频的评论
DOWMLOAD_VIDEO_REPLY = False

# 是否下载每个视频的弹幕
DOWMLOAD_VIDEO_BULLET = True

# 弹幕是否去重
BULLETSCREEN_IS_DISTINCT = True

#####################################################################  以下为保存设置

# up主的个人信息和概括的视频信息提供三种存储方式：mongo、json或CSV。若都不选则输出到标准流。
# 弹幕信息、评论信息提供两种存储方式：json或CSV。不支持输出到标准流。

# up主的个人信息和概括的视频信息是否保存到mongodb
SAVE_TO_MONGODB = False

# 是否保存成CSV文件
SAVE_TO_CSV = False

# 是否保存成json文件
SAVE_TO_JSON = True

# mongodb数据库地址
MONGO_URL = 'localhost'

# 数据库名称
MONGO_DB = 'bilibili'

# 保存up主们的个人信息的数据库表名
UPLOADER_INFO_MONGO_TABLE_NAME = 'uploaders'

# 保存up主们的个人信息的csv、json文件名
UPLOADER_INFO_CSV_FILE_NAME = 'uploaders'

# 保存up数据时是否使用up的uid作为文件名,否则使用up主昵称
# 为避免windows的名称不合法，会先将其合法化。下面同理
UES_MID_AS_FILE_NAME = False

# 保存视频数据时是否使用av号作为文件名,否则使用视频标题
UES_AV_AS_FILE_NAME = False

#####################################################################  以下为请求设置

# 是否使用UP主的UID查找，否则使用昵称查找(以下二选一)
# 建议False，昵称查找有可能错误
USE_NAME = True

# 待请求的UP主的UID
MID = 8776244

# 待请求的UP主的昵称
UPLOADER_NAME = '大大大灯泡'