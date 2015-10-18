#encoding:utf-8
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import dump
from datetime import datetime
from lxml import etree
import httplib2
import time
import random
import string
import hashlib
import json

import project_1.config

# xml格式的字符串 ==》 字典
def parse_Xml2Dict(raw_xml):
	xmlstr = etree.fromstring(raw_xml)
	dict_xml = {}
	for child in xmlstr:
		dict_xml[child.tag] = child.text.encode(u'UTF-8')
	return dict_xml

# 字典 ==》 xml格式的字符串
def parse_Dict2Xml(tag, d):
	elem = Element(tag)
	for key, val in d.items():
		child = Element(key)
		child.text = str(val)
		elem.append(child)
		
	my_str = tostring(elem, encoding = u'UTF-8')
	return my_str

# json样式的str ==> dict
def parse_Json2Dict(my_json):
	my_dict = json.loads(my_json)
	return my_dict

# dict ==> json样式的str
def parse_Dict2Json(my_dict):
	my_json = json.dumps(my_dict, ensure_ascii=False)
	return my_json
	
def my_get(url):
	h = httplib2.Http()
	resp, content = h.request(url, 'GET')
	return resp, content

def my_post(url, data):
	h = httplib2.Http()
	resp, content = h.request(url, 'POST', data)
	return resp, content
	
def dictfetchall(cursor):
	"Returns all rows from a cursor as a dict"
	"将自定义sql返回的列表转为字典 http://python.usyiyi.cn/django/topics/db/sql.html#executing-custom-sql-directly"
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]
	
def get_access_token():
	# 获取 access_token 存入 WEIXIN_ACCESS_TOKEN
	if project_1.config.WEIXIN_ACCESS_TOKEN_LASTTIME == 0 or (int(time.time()) - project_1.config.WEIXIN_ACCESS_TOKEN_LASTTIME > project_1.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN - 300):
	
		resp, result = my_get(project_1.config.WEIXIN_ACCESS_TOKEN_URL)
		decodejson = parse_Json2Dict(result)
		
		project_1.config.WEIXIN_ACCESS_TOKEN = str(decodejson[u'access_token'])
		project_1.config.WEIXIN_ACCESS_TOKEN_LASTTIME = int(time.time())
		project_1.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN = decodejson['expires_in']
		
		print "new access_token ->> " + project_1.config.WEIXIN_ACCESS_TOKEN + "---" + str(project_1.config.WEIXIN_ACCESS_TOKEN_LASTTIME) + "---" + str(project_1.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN)
		return project_1.config.WEIXIN_ACCESS_TOKEN
	else:
		print "old access_token ->> " + project_1.config.WEIXIN_ACCESS_TOKEN + "---" + str(project_1.config.WEIXIN_ACCESS_TOKEN_LASTTIME) + "---" + str(project_1.config.WEIXIN_ACCESS_TOKEN_EXPIRES_IN)
		return project_1.config.WEIXIN_ACCESS_TOKEN

def get_user_info(openid):
    ACCESS_TOKEN = get_access_token()
    resp, content = my_get('https://api.weixin.qq.com/cgi-bin/user/info?access_token='+ACCESS_TOKEN+'&openid='+openid+'&lang=zh_CN')
    return parse_Json2Dict(content)

def my_create_menu(menu_data):
    ACCESS_TOKEN = get_access_token()
    post_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + ACCESS_TOKEN
    post_data = parse_Dict2Json(menu_data)
    resp, content = my_post(post_url, post_data)
    return parse_Json2Dict(content)

def my_create_qrcode(data):
    ACCESS_TOKEN = get_access_token()
    post_url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=' + ACCESS_TOKEN
    post_data = parse_Dict2Json(data)
    resp, content = my_post(post_url, post_data)
    return parse_Json2Dict(content)

def send_text(touser, content):
    ACCESS_TOKEN = get_access_token()
    post_url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=' + ACCESS_TOKEN
    post_dict = {}
    post_dict['touser'] = touser
    post_dict['msgtype'] = "text"
    text_dict = {}
    text_dict['content'] = content
    post_dict['text'] = text_dict
    post_data = parse_Dict2Json(post_dict)
    my_post(post_url, post_data)

def create_timestamp():
    return int(time.time())

def create_nonce_str():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

# 获取访问者的真实IP地址
def get_user_real_ip(request):
    if request.META.has_key('HTTP_X_REAL_IP'):  
        return request.META['HTTP_X_REAL_IP']  
    else:  
        return request.META['REMOTE_ADDR']  

def get_jsapi_signature(noncestr, timestamp, url):
    jsapi_ticket = get_jsapi_ticket()
    data = {
        'jsapi_ticket': jsapi_ticket,
        'noncestr': noncestr,
        'timestamp': timestamp,
        'url': url,
    }
    keys = data.keys()
    keys.sort()
    data_str = '&'.join(['%s=%s' % (key, data[key]) for key in keys])
    signature = hashlib.sha1(data_str.encode('utf-8')).hexdigest()
    return signature

def create_out_trade_no():
    return str(int(time.time())) + random.randint(10000, 99999)
