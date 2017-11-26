# -*- coding: utf-8 -*-
# filename: handle.py
#在当前接口处理信息

import web
import hashlib
import reply
import receive

class Handle(object):
	def GET(self):
		try:
			data = web.input()
			if len(data) == 0:
				return 'hello to wechat' #whatever it is
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = '' #base information in wechat

			list = [token,timestamp,nonce]
			list.sort()
			sha = hashlib.sha1()
			map(sha.update,list)
			hashcode = sha.hexdigest()
			print('handle/GET func:hashcode, signature: ',hashcode,signature)
			if hashcode == signature :
				return echostr
			else:
				return ''  #whatever
		except Exception as Argument:
			return Argument

	def POST(self):
		try:
			webData = web.data()
			print('Handle POST webdata is ',webData)
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg,receive.Msg):
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName

				if recMsg.MsgType == 'text':
					content = 'test'   #reply the massage
					replyMsg = reply.TextMsg(toUser,fromUser,content)
					return replyMsg.send()
				if recMsg.MsgType == 'image':
					mediaId = recMsg.MediaId
					replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
					return replyMsg.send()
				else:
					print('暂不处理')
					return 'success'

			if isinstance(recMsg,receive.EventMsg):
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName

				if recMsg.Event == 'CLICK':
					content = u'尚未完成'.encode('utf-8')
					replyMsg = reply.TextMsg(toUser,fromUser,content)
					return replyMsg.send()
				else:
					print('暂不处理')
					return 'success'
		except Exception as Argment:
			return Argment