#_*_coding:utf-8_*_

from django import forms
from captcha.fields import CaptchaField


class CarTestForm(forms.Form):
	captcha = CaptchaField(label="验证码",error_messages={"invalid":"验证码错误"})

# Create your views here.
