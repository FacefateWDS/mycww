from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    line =' <h1 style="text-align:center">我的第一个网页！！！</h1>'
    line2 = '<hr>'
#    line3 = "<a herf = "/play/">开始</a>"
    line1 = '<img src ="https://tse1-mm.cn.bing.net/th/id/OIP-C.D9NM7OI_pGDC32kLDVhSAAHaE7?w=286&h=191&c=7&r=0&o=5&dpr=1.5&pid=1.7" width = 800 >'
    return HttpResponse(line+line1+line2)
