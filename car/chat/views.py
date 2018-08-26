from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message,create_reply
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature
from wechatpy import WeChatClient



client = WeChatClient('wx65ecd82cb1ce0559','9c5acf854e9fe944657c775ced596e81')
client.menu.create(
        {
        'button':[
                {
                'type':'click',
                'name':'汽车查询',
                'key':'car_find'
                },
        {
                'type':'click',
                'name':'车辆订单',
                'key':'car_dingdan'
        }
        ]
        }
)


WECHAT_TOKEN = 'slh201008'
@csrf_exempt
def weixin(request):
        if request.method == 'GET':
                signature = request.GET.get('signature','')
                timestamp = request.GET.get('timestamp','')
                nonce = request.GET.get('nonce','')
                echo_str = request.GET.get('echostr','')
                try:
                        check_signature(WECHAT_TOKEN,signature,timestamp,nonce)
                except InvalidSignatureException:
                        echo_str = 'error'
                response = HttpResponse(echo_str,content_type='text/plain')
                return response
        elif request.method == 'POST':
                msg = parse_message(request.body)
                if msg.type =="text":
                        reply = create_reply('A',msg)
                elif msg.type == 'image':
                        reply = create_reply('B',msg)
                elif msg.type == 'voice':
                        reply = create_reply('C',msg)
                else:
                        reply = create_reply('D',msg)
                response = HttpResponse(reply.render(),content_type='application/xml')
                return response
        else:
                logger.info('----------------')

# Create your views here.
