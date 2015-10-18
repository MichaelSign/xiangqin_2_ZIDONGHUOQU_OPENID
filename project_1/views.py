# coding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from project_1.forms import Register,RequestForm
from project_1.models import UserProfile
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

#from project_1.models import Female
#from project_1.models import Man

#----以示清晰-----------
import hashlib
import json
#from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import time
#import httplib2
from urllib import urlencode
from project_1.config import *
from project_1.my_function import *
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# Create your views here.
@csrf_exempt
def index(request):
        print "hello "
	"微信接入参考 http://mp.weixin.qq.com/wiki/17/2d4265491f12608cd170a95559800f2d.html"
	if request.method == "GET":
		signature	= request.GET.get("signature", None)
		timestamp	= request.GET.get("timestamp", None)
		nonce		= request.GET.get("nonce", None)
		echostr		= request.GET.get("echostr", None)
		# 放到数组中按字典序排序
		token		= WEIXIN_TOKEN
		tmp_list 	= [token, timestamp, nonce]
		tmp_list.sort()
		# 把三个字符串拼接在一起进行sha1加密
		tmp_str 	= "%s%s%s" % tuple(tmp_list)
		tmp_str		= hashlib.sha1(tmp_str).hexdigest()
		# 判断与传递进来的 signature 是否一致
		if tmp_str == signature:
			return HttpResponse(echostr)
		else:
                        print "index"
			return HttpResponse('index, GET sucess')
                #        return render(request,'index.html')
	elif request.method == "POST":
		raw_xml = request.body.decode(u'UTF-8')
		dict_str = parse_Xml2Dict(raw_xml)
		try:
			MsgType = dict_str['MsgType']
		except:
			MsgType = ''
		try:
			Event = dict_str['Event']
		except:
			Event = ''
		if MsgType == 'text':#当接收到用户发来的文本信息时
			res_dict = {}
                        print 'text'
			res_dict['ToUserName'] = dict_str['FromUserName']
			res_dict['FromUserName'] = dict_str['ToUserName']
			res_dict['CreateTime'] = int(time.time())
			res_dict['MsgType'] = 'text'
			res_dict['Content'] = dict_str['Content']
			echostr = parse_Dict2Xml('xml', res_dict)
			return HttpResponse(echostr)
		elif MsgType == 'image':
			send_text(dict_str['FromUserName'], "收到你发送的图片")
			return HttpResponse('')
		elif MsgType == 'voice':
			dict_user_info = get_user_info(dict_str['FromUserName'])
			print '------------------------------'
			print '发送语音的用户信息如下'
			print dict_user_info
			print dict_user_info['nickname'].encode('utf-8')
			print '------------------------------'
			return HttpResponse('')
		elif Event == 'subscribe':# 关注公众号事件
			if dict_str['EventKey'] and dict_str['Ticket']:# 通过扫描二维码进行关注
				qrcode_num = dict_str['EventKey'].split('_')[1]
				send_text(dict_str['FromUserName'], "感谢您的关注！" + str(qrcode_num))
			else:
				send_text(dict_str['FromUserName'], "感谢您的关注！")
			return HttpResponse('')
		elif Event == 'SCAN':
			send_text(dict_str['FromUserName'], "qrcode is " + str(dict_str['EventKey']))
			return HttpResponse('')
		elif MsgType == 'location':
			send_text(dict_str['FromUserName'], "你现在在:\n" + dict_str['Label'])
			return HttpResponse('')
		else:
			return HttpResponse('')
		
		
def create_menu(request):
    "在微信公众号创建菜单，这个请求是要我们主动发起"
    print 'create_menu'
    menu_data = {}
    button1 = {}
    button1['name'] = '1个人信息'
    button1['type'] = 'view'
    #button1['url']='https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/test/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button1['url']='https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/user_info/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'


    button2 = {}
    button2['name'] = 'test2.html'
    button2['type'] = 'view'
    button2['url'] = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='+WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/test2/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button3 = {}
    button3['name'] = '3'
    #button3['type'] = 'view'
    #button3['url'] = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='+WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/test3/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button31 = {}
    button31['name'] = 'test1'
    button31['type'] = 'view'
    button31['url'] = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/test/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button32 = {}
    button32['name'] = 'test3'
    button32['type'] = 'view'
    button32['url'] = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='+WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/test3/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button33 = {}
    button33['name'] = '我的二维码'
    button33['type'] = 'view'
    button33['url'] = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid='+WEIXIN_APPID + '&redirect_uri=http://101.200.205.241/project_1/qrcode/?num=1/&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
    button3['sub_button'] = [button31, button32, button33]

    menu_data['button'] = [button1, button2, button3]
    
    post_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+get_access_token()
    post_data = parse_Dict2Json(menu_data)
    resp, content = my_post(post_url, post_data)
    response = parse_Json2Dict(content)
  #print post_url
    #response = my_create_menu(menu_data)
    if response['errcode'] == 0:
    	return HttpResponse('create menu OK')
    else:
    	return HttpResponse(WEIXIN_ACCESS_TOKEN+'create menu err:' + response['errmsg'])
    	#return HttpResponse('create menu err:' + response['errmsg'])

def user_info(request):
    code = request.GET.get('code', '')
    if code == '':
        return HttpResponse('请您先授权')
    scope = request.GET.get('scope', None)
    
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='+WEIXIN_APPID+'&secret='+WEIXIN_APPSECRET+'&code='+code+'&grant_type=authorization_code'
    resp, content = my_get(url)
    dict_user = parse_Json2Dict(content)
    print scope
    #if state == 'snsapi_base':
       # return render(request, 'user_info.html', dict_user)
    #if state == 'snsapi_userinfo':
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token='+dict_user['access_token']+'&openid='+dict_user['openid']+'&lang=zh_CN'
    res, content = my_get(url)
    dict_user2 = parse_Json2Dict(content)
    dict_user.update(dict_user2)
    return render(request, 'project_1/user_info.html', dict_user)

    #return HttpResponse('err: state')

def qrcode(request):
    value_number = request.GET.get('num', None)
    if not value_number:
        return HttpResponse('<h1>你需要在网址的后面加上num参数。如：...?num=1</h1>')
    data = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": value_number}}}
    my_dict = my_create_qrcode(data)
    my_dict['num'] = value_number
    return render(request, 'project_1/qrcode.html', my_dict)

# Create your views here.


#----以示清晰----
def test(request) :
	context_dict = {}
	return render(request, 'project_1/test.html')

def test2(request):
	context_dict={}
	try:
		'''
		female = Female.objects.all()
		man = Man.objects.all()
		context_dict['female'] = female 
		context_dict['man'] = man 
		'''

		userProfile = UserProfile.objects.all()
		context_dict['userProfile'] = userProfile
	except UserProfile.DoesNotExist:
		pass 

	return render_to_response( 'project_1/test2.html',context_dict)
'''
def test3(request) :
	if request.method == 'POST' :
		form = Register(request.POST)
		if form.is_valid() :
			form.save()
			print form.cleaned_data
			return render(request, 'project_1/test.html')
		else :
			print form.errors
	else :
		form = Register()
	return render(request, 'project_1/test3.html', {'form' : form})
'''

def test3(request) :
	if request.method == 'POST' :
		userform = Register(request.POST)
		#print request.POST
		if userform.is_valid() :
			userform.save()
#------------------------------------------------------------------------------
			request.session['OpenID'] = request.POST.get('OpenID')
#------------------------------------------------------------------------------

			#print userform.cleaned_data
			#return render(request,'project_1/test.html')
			#return HttpResponseRedirect('project_1/requestInfo.html')
			#return render_to_response('project_1/requestInfo.html')
			#return render(request,'project_1/requestInfo.html')
			#return HttpResponseRedirect()
			return render(request,'project_1/requestInfo.html',{'requestform':RequestForm()})
		else :
			print userform.errors
	else :
		userform = Register()
	return render(request,'project_1/test3.html', {'userform' : userform})


Mes = "%s;%s;%s;%s;%s;%s;%s;%s"

def requestInfo(request):
    if request.method == 'POST' :
        requestform = RequestForm(request.POST)
        if requestform.is_valid():
            #get infomation from POST
            sex = request.POST.get('sex',False)
            ages = request.POST.get('ages',False)
            height = request.POST.get('height',False)
            weight = request.POST.get('weight',False)
            hometown = request.POST.get('hometown',False)
            education = request.POST.get('education',False)
            Occupation = request.POST.get('Occupation',False)
            aim = request.POST.get('aim',False)
            #
            #info = sex + '_'+ages + '_'+height+'_'+weight+'_'+hometown+'_'+education+'_'+Occupation+'_'+aim
            #print requestform
            info = Mes % (sex, ages,height,weight,hometown,education,Occupation,aim)
            #print info 
            #return 
            UserProfile.objects.filter(OpenID=request.session.get('OpenID',False)).update(require = info)

            #db = sqlite3.connect(user='itcast',db='db.sqlite3',password='123',charset='utf-8')
            #db = sqlite3.connect("../db.sqlite3")
            #cursor = connection.cursor()
            #cursor.execute("UPDATE UserProfile SET Require = info where OpenID='3333'")
            #cursor.execute("SELECT * FROM User")
           #transaction.commit_unless_managed()
            #db.close()
            return resInfo(request)

        else:
            print requestform.errors
    else:
        requestform = RequestForm()

    return render(request,'project_1/requestInfo.html',{'requestform':requestform})


#############################################################
AGES = {'a':(0,17),
    'b':(18,22),
    'c':(23,26),
    'd':(27,35),
    'e':(35,200), 
    }

EDUS={
    1:'初中',
    2:'高中',
    3:'大专',
    4:'大本',
    5:'硕士',
    6:'博士',
        }

def getAllObjects(P_require) :
    ''' P_require Each search condition to ';' Separated
        A total of 7 ';'  
        "sex;ages;height;weight;hometown;education;Occupation;aim"
         -- http://www.bing.com/translator/ '''

    Sel = 'SELECT * FROM project_1_UserProfile WHERE %s'
    req_list = P_require.split(';')
    res = ''
    if req_list[0] :
        res+='sex="%s" and ' % (req_list[0])
    if req_list[1] :
        res+='age >= %d and age <= %d and ' % (AGES[req_list[1]][0], AGES[req_list[1]][1])
            # can't use age in (%d,%d) 
    if req_list[2] :
        res += 'height>=%s and ' %(req_list[2])
    if req_list[3] :
        res += 'weight>=%s and ' %(req_list[3])
    if req_list[4] :
        res += 'hometown="%s" and ' % (req_list[4])
    if req_list[5] :
        res += 'education >= %s and ' % (req_list[5])
    if req_list[6] :
        res += 'Occupation="%s" and ' %(req_list[6])

    if not res.strip(): 
        # res is null or '' 
        res = '1 = 0 '
    else :
        res += '1 = 1'

    res = Sel % (res)
    ret = UserProfile.objects.raw(res)
    return ret  

def getResObjects(objs, src) :
    '''
    objs : The values found in the database contains 'require'
    xx.require : "sex;ages;height;weight;hometown;education;Occupation;aim"
    src : The values use found objs in the database 
    ret list 
    '''
    ret = []
    for obj in objs :
        req_list = obj.require.split(';')
        if req_list[0] and req_list[0] != src.sex:
            continue
        if req_list[1] and (src.age < AGES[req_list[1]][0] or src.age > AGES[req_list[1]][1]) :
            continue
        if req_list[2] and int(req_list[2]) > src.height:
            continue
        if req_list[3] and int(req_list[3]) > src.weight:
            continue
        if req_list[4] and req_list[4] != src.hometown :
            continue
        if req_list[5] and req_list[5] < int(src.education):
            continue
        if req_list[6] and  req_list[6] != src.Occupation:
            continue
        ret.append(obj)
        ret[len(ret)-1].education =  EDUS[ret[len(ret)-1].education]
    return ret 



#############################################################
def resInfo(request):
    '''
    if request.method == 'POST':
        print request.POST
    else:
        preUser = UserProfile.objects.get(OpenID=request.session.get('OpenID',False))
        getAllObjects(preUser.require)
        print "11111"
        return 
    '''
    preUser = UserProfile.objects.get(OpenID=request.session.get('OpenID',False))
    m_objects = getAllObjects(preUser.require)
    #print [x.name for x in m_objects]
    list_res = getResObjects(m_objects, preUser)
    return render(request,'project_1/resInfo.html',{'list_res':list_res})


"""
'''
        reqInfo = preUser.require
        print reqInfo
        
        req_list = reqInfo.split(';')
        sex = req_list[0]
        ages = req_list[1] 
        height = req_list[2]
        weight = req_list[3]
        hometown = req_list[4]
        education = req_list[5]
        Occupation = req_list[6]
        aim = req_list[7]
        '''
        '''
        list_res = []
        res_object = UserProfile.objects.filter(sex=sex)
        for res in res_object:
            reqInfo_other = res.require

            req_otherlist = reqInfo_other.split(';')

            oth_sex = req_otherlist[0]
            oth_ages = req_otherlist[1]
            oth_height = req_otherlist[2]
            oth_weight = req_otherlist[3]
            oth_hometown = req_otherlist[4]
            oth_education = req_otherlist[5]
            oth_Occupation = req_otherlist[6]
            oth_aim = req_otherlist[7]

            if oth_sex == preUser.sex:
                list_res.append(res)
    return render(request,'project_1/resInfo.html',{'list_res':list_res})
    '''
"""

def detail(request,detail_slug):
    context_dict = {}
    try:
        she_he = UserProfile.objects.get(OpenID=detail_slug)
        context_dict['she_he'] = she_he
    except UserProfile.DoseNotExist:
        pass
    return render(request,'project_1/detail.html',context_dict)


    #---------------------以示清晰------------------

