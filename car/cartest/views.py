#_*_encoding:utf-8_*_

from django.shortcuts import render,HttpResponse
from cartest.forms import CarTestForm
from cartest.models import Carinfo
from django.views.generic.base import View
from django.core.mail import send_mail #引入发送邮件send_mail函数
from car.settings import EMAIL_FROM   

from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json

def ajax_val(request):
	if request.is_ajax():
		cs = CaptchaStore.objects.filter(response=request.GET['response'],hashkey=request.GET['hashkey'])
		if cs:
			json_data = {'status':1}
		else:
			json_data = {'status':0}
		return JsonResponse(json_data)
	else:
		json_data = {'status':0}
		return JsonResponse(json_data)

def captcha_refresh(request):
	if not request.is_ajax():
		return HttpResponse("404")
	new_key = CaptchaStore.generate_key()
	to_json_response = {
		'key':new_key,
		'image_url':captcha_image_url(new_key),
	}
	return HttpResponse(json.dumps(to_json_response),content_type='application/json')



email = "18814124132@139.com"
email_title = "您有一条新的检测订单" 

class Index(View):
	def get(self,request):
		form = CarTestForm()
		hashkey = CaptchaStore.generate_key()
		image_url = captcha_image_url(hashkey)
		return render(request,"cartest/index.html",locals())
	def post(self,request):
		Username = request.POST["Username"]
		phone_number = request.POST["phone_number"]
		car_number = request.POST["car_number"]
		address = request.POST["address"]
		form = CarTestForm(request.POST)
		if form.is_valid():
			if Carinfo.objects.filter(car_number=car_number):
				msg = "您输入的车辆已存在"
				return render(request,"cartest/index.html",locals())
			else:
				New_msg = Carinfo()
				New_msg.Username = Username
				New_msg.phone = phone_number
				New_msg.car_number = car_number
				New_msg.address = address
				New_msg.save()
				msg = "您的信息已提交"
				email_body = "车主：%s，车牌号码：%s,电话：%s，取车地址：%s"%(Username,car_number,phone_number,address)
				send_mail(email_title,email_body,EMAIL_FROM,[email])
				return render(request,"cartest/index.html",locals())
		else:
			msg = "验证码错误"
			return render(request,"cartest/index.html",locals())

'''		
def index(request):
	if request.method =="GET":
		cartestform = CarTestForm()
		return render(request,"cartest/index.html",locals())
	if request.method =="POST":
		cartestform = CarTestForm(request.POST)
		if cartestform.is_valid():
			Username = cartestform.cleaned_data["Username"]
			phone = cartestform.cleaned_data["phone"]
			car_number = cartestform.cleaned_data["car_number"]
			address = cartestform.cleaned_data["address"]
			if Carinfo.objects.filter(car_number=car_number):
				cartestform = CarTestForm()
				error_msg = "您的汽车已存在系统"
				return render(request,"cartest/index.html",locals())
			else:
				car = Carinfo()
				car.Username = Username
				car.phone = phone
				car.car_number = car_number
				car.address = address
				car.save()
				return HttpResponse("提交成功")
		else:
			cartestform = CarTestForm()
			return render(request,"cartest/index.html",locals())
'''
# Create your views here.
