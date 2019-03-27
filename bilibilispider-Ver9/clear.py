'''
一键删除所有文件夹数据
'''

import os

def file_remove():
	total_dirpath = 'download'

	for each in os.listdir(total_dirpath):
		each_dir = '{}\\{}'.format(total_dirpath,each)
		for file in os.listdir(each_dir):
			os.remove('{}\\{}'.format(each_dir,file))
			print('删除文件：{}\\{}'.format(each_dir,file))


if __name__ == '__main__':
	file_remove()