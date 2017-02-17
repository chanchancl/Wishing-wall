
from django.utils import timezone
from wishingwall.models import VisitData, AddVisitCount

_DEBUG = False

def debug_log(str):
    if _DEBUG:
        print(str)

debug_log('You had install count.')

'''
可保存的信息有:
1.META['REMOTE_ADDR']   访问网站的IP地址
2.META['HTTP_USER_AGENT']  用户的浏览器
'''
# in second
_MAX_PASSED_DELTA = 3600


class count_middleware(object):
    def __init__(self):
        self._ipDict = {}

    def process_request(self, request):
        debug_log('Where am I?')
        return None

    def process_response(self, request, response):
        debug_log('process_response')
        debug_log(request)
        debug_log(response)
        ip = request.META['REMOTE_ADDR']

        if 'visit_time' in request.COOKIES:
            # 老访客
            pass
        else:
            # 新访客
            if  request.path.split('/')[1] != 'admin':
                now = timezone.now()
                if ip in self._ipDict:
                    dt = timezone.datetime.strptime(self._ipDict[ip],'%Y-%m-%d-%H-%M')
                    delta = now - dt
                    if delta.second > _MAX_PASSED_DELTA:
                        self._ipDict[ip] = now.strftime('%Y-%m-%d-%H-%M')
                        Visit(request, response)
                else:
                    self._ipDict[ip] = now.strftime('%Y-%m-%d-%H-%M')
                    Visit(request, response)

        return response


def Visit(request, response):
    dt = timezone.now()
    expr = dt + timezone.timedelta(seconds=_MAX_PASSED_DELTA)
    response.set_cookie('visit_time', dt, expires=expr)
    visit = VisitData.objects.create(ipAddress=request.META[
                                     'REMOTE_ADDR'], userAgent=request.META['HTTP_USER_AGENT'], dateTime=dt)
    AddVisitCount()
    debug_log(visit)
