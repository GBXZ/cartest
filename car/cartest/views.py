from django.shortcuts import render,HttpResponse
from cartest.forms import CarTestForm
from cartest.models import Carinfo
from django.views.generic.base import View


class Index(View):
	def get(self,request):
		index_form = CarTestForm()
		return render(request,"cartest/index.html",locals())
	def post(self,request):
		Username = request.POST["Username"]
		phone_number = request.POST["phone_number"]
		car_number = request.POST["car_number"]
		address = request.POST["address"]
		index_form = CarTestForm(request.POST)
		if index_form.is_valid():
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
				return HttpResponse("OK")
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
