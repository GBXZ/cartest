#_*_encoding:utf-8_*_

from django.shortcuts import render,HttpResponse
from cartest.forms import CarTestForm
from cartest.models import Carinfo
from django.views.generic.base import View
from django.core.mail import send_mail #引入发送邮件send_mail函数
from car.settings import EMAIL_FROM   



email = "18814124132@139.com"
email_title = "您有一条新的检测订单" 

class Index(View):
	def get(self,request):
		return render(request,"cartest/index.html",locals())
	def post(self,request):
		Username = request.POST["Username"]
		phone_number = request.POST["phone_number"]
		car_number = request.POST["car_number"]
		address = request.POST["address"]
		fan_address = request.POST["fan_address"]
		if Carinfo.objects.filter(car_number=car_number):
			msg = "您输入的车辆已存在"
			return render(request,"cartest/index.html",locals())
		else:
			New_msg = Carinfo()
			New_msg.Username = Username
			New_msg.phone = phone_number
			New_msg.car_number = car_number
			New_msg.address = address
			New_msg.fan_address = fan_address
			New_msg.save()
			msg = "您的信息已提交"
			email_body = "车主：%s，车牌号码：%s,电话：%s，取车地址：%s,还车地址：%s"%(Username,car_number,phone_number,address,fan_address)
			send_mail(email_title,email_body,EMAIL_FROM,[email])
			return render(request,"cartest/index.html",locals())

# Create your views here.
