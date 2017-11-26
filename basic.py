# -*- coding: utf-8 -*-
# filename: basic.py
#获取微信借口token凭证

import time
import json
import requests

class Basic(object):
	def __int__(self):
		self.__accessToken = ''
		self.__leftTime = 0
	def __real_get_access_token(self):
		appId = ''  #服务器在微信后台上的信息
		appSecret = ''

		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=""client_credential&appid=%s&secret=%s" % (appId, appSecret))
		urlResp = reqeusts.post(postUrl)
		urlResp = json.loads(urlResp.content)

		self.__accessToken = urlResp['access_token']
		self.__leftTime = urlResp['expires_in']

	def get_access_token(self):
		if self.__leftTime < 10
			self.__real_get_access_token()
		return self.__accessToken

	def run(self):
		while(True):
			if self.__leftTime > 10:
				time.sleep(2)
				self.__leftTime -= 2
			else:
				self.__real_get_access_token()
