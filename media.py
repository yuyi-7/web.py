# -*- coding: utf-8 -*-
# filename: media.py
#上传或者下载临时素材到微信以回复素材到用户

from basic import Basic
import requests
import json
import time
import os


class Media(object):
	def __int__(self):
		pass
	def upload(self,accessToken,filepath,mediaType):
		file = open(filepath,'rb')
		param = {'media':file}

		postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
		request = requests.post(postUrl,files = param)
		print(request.text)

	def get(self,accessToken,mediaId,filepath):
		postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
		urlResp = requests.get(postUrl)

		headers = urlResp.headers
		if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
			jasondict = json.loads(urlResp.text)
			print(jasondict)
		else:
			buffer = urlResp.text   #素材的二进制
			mediaFile = open(os.path.join(filepath,"media_%s.jpg"%(time.strftime('%H-%M-%S'))), "wb")
			mediaFile.write(buffer)
			print("get successful")

if __name__ == '__main__':
	myMedia = Media()
	accessToken = Basic().get_access_token()
	chioce = input('请输入选择是get还是upload素材：')
	if chioce == 'upload':
		filepath = input('请输入临时素材绝对路径：')
		mediaType = input('请输入素材类型(如图片:image)：')
		myMedia.upload(accessToken,filepath,mediaType)
	elif chioce == 'get':
		mediaid = input('请输入素材的MediaId：')
		filepath = input('请输入要保存文件的路径，若不输入默认保存本目录temp文件：')
		if filepath == '':
			filepath = os.path.join(os.path.abspath('.'),'temp')
		myMedia.get(accessToken,mediaid,filepath)

	"""
	如果想使用临时素材，可以用其MediaId使用
	如果想手动下载用户提交的临时素材，可以用
	https://api.weixin.qq.com/cgi-bin/media/get?access_token=ACCESS_TOKEN&media_id=MEDIA_ID （自行替换数据）
	"""