from django.contrib import admin
from cartest.models import Carinfo
import xadmin
from xadmin import views

class CarinfoAdmin(object):
	list_display=['Username','phone','car_number','address','car_state','create_time','change_time']
	search_fields=("Username","phone","car_number","address")
	list_filter=('Username','phone','car_number','address','car_state','create_time','change_time')

class BaseSetting(object):
	enable_themes=True
	use_bootswatch=True

class GlobalSettings(object):
	site_title="汽车检测管理系统"
	site_footer="汽车检测"
	
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Carinfo,CarinfoAdmin)
# Register your models here.
