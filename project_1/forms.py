#coding:utf-8
from django import forms
from django.contrib.auth.models import User
from project_1.models import UserProfile

AGES = {'a':(0,17),
	'b':(18,22),
	'c':(23,26),
	'd':(27,35),
	'e':(35,200), 
	}

	# when you find in data
	# Associations top  'AGES'

SOURCES_AGES=(
       ('a','18以下'),
       ('b','18-22'),
       ('c','23-26'),
       ('d','27-35'),
       ('e','35'),
        )

SOURCES_EDU=(
	(1,'初中'),
	(2,'高中'),
        	(3,'大专'),
        	(4,'大本'),
        	(5,'硕士'),
        	(6,'博士'),
        )

SOURCES_AIM=(
        ('friend','交友'),
        ('marry','结婚'),
        )

SOURCES_CHOICES=(
	('m','boy'),
	('f','girl'),
	)


class Register(forms.ModelForm) :
	required_css_class = 'register'
	name = forms.CharField(label="姓名",max_length=50)
	sex = forms.ChoiceField(label=("性别"), widget=forms.Select(), choices=SOURCES_CHOICES,initial=SOURCES_CHOICES[1])
	age = forms.IntegerField(label="年龄", initial=0)
	education = forms.ChoiceField(label="学历",widget=forms.Select(),choices=SOURCES_EDU,initial=SOURCES_EDU[1])

	Occupation = forms.CharField(label="职业")
	height =forms.IntegerField(label="身高")
	weight = forms.IntegerField(label="体重")
	BJHouseholds = forms.BooleanField(label="JH",required=False)
	car =  forms.BooleanField(label="车子",required=False)
	house = forms.BooleanField(label="房子",required=False)
	hometown = forms.CharField(label="家乡",max_length=1024)

	require = forms.CharField(widget=forms.HiddenInput(),max_length=8096,required=False)
	flag = forms.BooleanField(widget=forms.HiddenInput(),required = False)
	WxNo = forms.CharField(widget=forms.HiddenInput(),max_length=128,required=False)
	img = forms.ImageField(widget=forms.HiddenInput(), required=False)
	message = forms.CharField(max_length=8096,widget=forms.HiddenInput(),required=False)
	QqNo = forms.CharField(max_length = 128,widget=forms.HiddenInput(),required=False)
	location = forms.CharField(max_length = 1024,widget=forms.HiddenInput(),required=False)
	Character = forms.CharField(max_length = 128,widget=forms.HiddenInput(),required=False)
	views = forms.IntegerField(widget=forms.HiddenInput(),required=False,initial=0)
	synopsis = forms.CharField(max_length=128,widget=forms.HiddenInput(),required=False)

	OpenID = forms.CharField(max_length = 128)

	class Meta:
		model=UserProfile
		#field=('name','sex','age','education','Occupation','height','weight','BJHouseholds','car','house','hometown')
		fields = '__all__'


class RequestForm(forms.Form):
    sex = forms.ChoiceField(label='性别',choices=SOURCES_CHOICES,initial=SOURCES_CHOICES[1])
    ages = forms.ChoiceField(label='年龄段',choices=SOURCES_AGES,initial=SOURCES_AGES[1])
    height = forms.IntegerField(label="身高")
    weight = forms.IntegerField(label="体重")
    hometown = forms.CharField(label="家乡",max_length=1024, required=False, initial='')
    education = forms.ChoiceField(label="学历",widget=forms.Select(),choices=SOURCES_EDU,initial=SOURCES_EDU[1])
    Occupation = forms.CharField(label="职业", required=False,initial='')
    aim = forms.ChoiceField(label="动机",widget=forms.Select(),choices=SOURCES_AIM,initial=SOURCES_AIM[1])
   



'''
	require = forms.CharField(widget=forms.HiddenInput(),max_length=8096,required='',initial=' ')
	flag = forms.BooleanField(widget=forms.HiddenInput(),required = False, initial=False)
	WxNo = forms.CharField(widget=forms.HiddenInput(),max_length=128,required='', initial=' ')
	img = forms.ImageField(widget=forms.HiddenInput(), required='',initial='')
	message = forms.CharField(max_length=8096,widget=forms.HiddenInput(),required='', initial=' ')
	QqNo = forms.CharField(max_length = 128,widget=forms.HiddenInput(),required='', initial=' ')
	location = forms.CharField(max_length = 1024,widget=forms.HiddenInput(),required='', initial=' ')
	Character = forms.CharField(max_length = 128,widget=forms.HiddenInput(),required='', initial=' ')
	views = forms.IntegerField(widget=forms.HiddenInput(),required=0, initial=0)
	synopsis = forms.CharField(max_length=128,widget=forms.HiddenInput(),required='', initial=' ')
'''



"""#coding:utf-8
from django import forms
from django.contrib.auth.models import User
from project_1.models import UserProfile

SOURCES_CHOICES=(
	('m','boy'),
	('f','girl'),
	)

class Register(forms.ModelForm) :
	required_css_class = 'register'
	sex = forms.ChoiceField(label=("性别"), widget=forms.Select(), choices=SOURCES_CHOICES,
		initial=SOURCES_CHOICES[1])
	name = forms.CharField(label=("Username"), max_length=30, help_text=("Register"))
	car = forms.BooleanField(required=False,initial=True)
	OpenID = forms.CharField(label=("OpenID"), max_length =128)

	class Meta:
     		model = UserProfile
"""


"""
'''
E = 'e'
A = 'a'
SOURCES_CHOICES = (
	(A, 'A'),
	(E, 'E'),
	)
'''
SOURCES_CHOICES = (
	('f', '女' ),
	('m', '男' ),
	)
	# (get value, show in page)


class Register(forms.Form) :
	required_css_class = 'register'
	username = forms.CharField(label=("Username"), max_length=30, help_text=("Register"))
	provider = forms.ChoiceField(widget=forms.Select(), choices=SOURCES_CHOICES,
		initial=SOURCES_CHOICES[1])
	car = forms.BooleanField(required=False)
"""

'''
error
FAVORITE_COLORS_CHOICES =({'sex' : 'f'}, {'sex' : 'm'})

class Register(forms.Form) :
	sex = forms.ChoiceField(label=u'FM',
		choices=FAVORITE_COLORS_CHOICES)
	name = forms.CharField(max_length=100)
'''