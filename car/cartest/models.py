#_*_encoding:utf-8_*_
from datetime import datetime

from django.db import models

class Carinfo(models.Model):
	Username = models.CharField(max_length=50,verbose_name=u"用户名")
	phone = models.CharField(max_length=100,verbose_name=u"手机号码")
	car_number = models.CharField(max_length=100,verbose_name=u"车牌号码",unique=True)
	address = models.CharField(max_length=200,verbose_name=u"地址")
	fan_address = models.CharField(max_length=200,verbose_name = u"还车地址",default = "")
	car_state = models.CharField(max_length=10,choices=(('dj','待检测'),('jc','检测中'),('yj','已检测')),default="dj",verbose_name="汽车状态")
	create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	change_time = models.DateTimeField(auto_now=True,verbose_name="最后修改时间")
	
	class Meta:
		verbose_name=u"车辆信息"
		verbose_name_plural =verbose_name
		
	def __str__(self):
		return self.car_number
# Create your models here.
