from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
from Server.models import LoginUser,ApiToken,Server
import json
import time
import datetime
import hashlib

class API(View):
    """
    对于接口上传或者下载数据我们需要进行login登录
       Request：
      {
          “type”:“user_login”,
           “data”: {
                 “username”：“while”,
                  “password”: “123”
            },
            “token”: “”
        }
        Response：
                {
                  “status”:“success”,
                   “data”: {
                         “token” : “k123jk12kl3j12jk1j3l12”
            }
        }
        登录成功，创建token，返回
        login_example = {
            "type":"user_login",
            "data": {
                "username": "while ",
                "password": "123"
            },
            "token": ""
            }
    """
    def __init__(self,**kwargs):
        View.__init__(self,**kwargs)
        self.result = {
            "status":"",
            "data":{}
        }
    def post(self,request):
        """
        处理post请求
        """
        if request.POST:
            postType = request.POST.get("type")
            postData = json.loads(request.POST.get("data"))
            if postType == "user_login":
                if postData:
                    username = postData.get("username")
                    password = postData.get("password")
                    try:
                        loginUser = LoginUser.objects.get(username = username)
                    except:
                        self.result["status"] = "error"
                        self.result["data"]["error"] = "no method named %s" % username
                    else:
                        db_password = loginUser.password
                        if password == db_password:
                            try:
                                db_token = ApiToken.objects.get(user_id=loginUser.id)
                            except:
                                token = self.makeToken(username)
                                t = ApiToken()
                                t.value = token
                                t.time = datetime.datetime.now()
                                t.user_id = loginUser.id
                                t.save()
                                # ApiToken.objects.create(
                                #     value = new_token,
                                #     time = datetime.datetime.now(),
                                #     user_id = loginUser.id
                                # )
                                self.result["status"] = "success"
                                self.result["data"]["token"] = token
                            else:
                                db_time_tuple = db_token.time.timetuple()
                                db_time_stamp = time.mktime(db_time_tuple)
                                now_time_tupe = datetime.datetime.now().timetuple()
                                now_time_stamp = time.mktime(now_time_tupe)

                                if 0 < now_time_stamp - db_time_stamp < 3600:
                                    self.result["status"] = "error"
                                    self.result["data"]["error"] = "you have token: %s" % db_token.value
                                    # 如果token失效，就再次生成
                                else:
                                    token = self.makeToken(username)  # 生成token

                                    db_token = datetime.datetime.now()
                                    db_token.value = token
                                    db_token.save()

                                    self.result["status"] = "success"
                                    self.result["data"]["token"] = token
                        else:  # 比对失败，密码不正确
                            self.result["status"] = "error"
                            self.result["data"]["error"] = "%s's error is wrong" %username
                else:
                    self.result["status"] = "error"
                    self.result["data"]["error"] = "empty error"
            elif postType == "addServer":
                if postData:
                    postToken = request.POST.get("token")  # 获取接口请求的数据
                    if postToken and self.tokenValid(postToken) == "ok":
                        # 获取数据
                        ip = postData.get("ip")
                        mac = postData.get("mac")
                        cpu = postData.get("cpu")
                        memory = postData.get("memory")
                        disk = postData.get("disk")
                        # 保存数据
                        server = Server()
                        server.ip = ip
                        server.mac = mac
                        server.cpu = cpu
                        server.memory = memory
                        server.disk = disk
                        server.isalive = "false"
                        server.save()
                        # Server.objects.create(
                        #     ip = ip,
                        #     mac = mac,
                        #     cpu = cpu,
                        #     memory = memory,
                        #     hostname = hostname,
                        #     isalive = "false"
                        # )
                        # 发送返回
                        self.result["status"] = "success"
                        self.result["data"]["result"] = "save success"
                    else:
                        self.result["status"] = "error"
                        self.result["data"]["result"] = self.tokenValid(postToken)
                else:
                    self.result["status"] = "error"
                    self.result["data"]["error"] = "data error"
            else:
                self.result["status"] = "error"
                self.result["data"]["error"] = "no method named %s"%postData
            return JsonResponse(self.result)

    def get(self, request):
        """
        处理get请求
        """
        if request.GET:
            getData = request.GET.get("key")
            return HttpResponse(getData)

    def makeToken(self, username):
        """
            md5算法生成token
        """
        time_stamp = str(time.time())  # 获取当前时间的时间的时间戳，然后转换为字符串
        value = username + time_stamp  # 将值和时间戳字符进行拼接

        md5 = hashlib.md5()
        md5.update(value.encode())
        token = md5.hexdigest()
        return token

    def tokenValid(self, token):
        # 校验存在
        try:
            db_token = ApiToken.objects.get(value=token)
        except:
            return "token error"
        else:
            # 校验过期
            db_time_tuple = db_token.time.timetuple()
            db_time_stamp = time.mktime(db_time_tuple)  # 数据库时间的时间戳

            now_time_tupe = datetime.datetime.now().timetuple()
            now_time_stamp = time.mktime(now_time_tupe)  # 当前时间的时间戳
            if 0 < now_time_stamp - db_time_stamp < 3600:
                return "ok"
            else:
                db_token.delete()
                return "time out"

def serverList(request):
    return render(request,"get_server_page.html")

def setPage(page,one_time_page,one_page_data,db):
    '''就是进行分页，分页的公共用法'''
    db_data = db.objects.all()#获取指定数据库的所有数据
    if page/one_time_page > int(page/one_time_page):
        findIndex = int(page/one_time_page) + 1
    else:
        findIndex = int(page/one_time_page)
    # 进行第一次查询，每次查询5页，每页4条的数据
    select_data = one_page_data * one_time_page#这里决定一次查询20条
    select_start = (findIndex - 1) * select_data#开始查询的索引
    select_end = findIndex * select_data#结束查询的索引

    select_range = db_data[select_start:select_end]#这里查询出了一次20条数据

    now_index = page - (findIndex - 1) * one_time_page
    # 设定单页的截取起始
    page_start = (now_index - 1) * one_page_data
    page_end = now_index * one_page_data
    # 开始截取
    page_data = select_range[page_start:page_end]
    result = {
        "page":page,
        "page_data":page_data
    }
    # 页码处理
    # page 1  page_range[1,2,3,4,5]
    # page 2  page_range[1,2,3,4,5]
    # page 3  page_range[1,2,3,4,5]
    # page 4  page_range[2,3,4,5,6]   [page-2:page+3]
    # page 5  page_range[3,4,5,6,7]   [page-2:page+3]
    # page 6  page_range[4,5,6,7,8]   [page-2:page+3]
    # 还要考虑超出范围的问题，为此我们写下以下代码
    count = db.objects.count()#数据总条数
    all_page = count/one_page_data
    if all_page != int(all_page):#如果不能整除，加1
        all_page += 1
    all_page = int(all_page)#转换为整形
    #定义判断页面的范围
    islast = 0
    if page >= all_page:
        page = all_page
        islast = 1
    # 获取页码
    if page in [1,2,3]:
        prange_start = 1
        prange_end = 6
    else:
        prange_start = page - 2
        prange_end = page + 3
    if prange_end >= all_page:
        prange_end = all_page
    prange = list(range(prange_start,prange_end))#python3 range返回的不是列表
    result["count"] = count #总条数
    result["pageRange"] = prange #页码
    result["islast"] = islast #是否是最后一页
    return result

def serverData(request):
    if request.method == "GET" and request.GET:
        page = int(request.GET.get("page"))

        one_page_data = 4
        one_time_page = 5

        result_list = []
        page_data = setPage(page,one_time_page,one_page_data,Server)

        datas = page_data.get("page_data")
        for data in datas:
            result_list.append(
                {
                    "id":data.id,
                    "ip": data.ip,
                    "mac": data.mac,
                    "cpu": data.cpu,
                    "memory": data.memory,
                    "disk": data.disk,
                    "isalive": data.isalive
                }
            )
        page_data["page_data"] = result_list
        return JsonResponse(page_data)
    else:
        return JsonResponse({"error":"no data"})


def gateoneConnection(request):
     return render(request,"gateoneConnection.html")


def gateoneConnectionV2(request):
    if request.method=="GET" and request.GET:
        ip = request.GET.get("ip","192.168.21.66")
        port = request.GET.get("port","22")
        user = request.GET.get("user","root")

        return render(request, "gateoneConnection_V2.html")
    else:
        return HttpResponse("404,there is no page for you")
import hmac
def gateValid(request):
    gateone_server = "https://192.168.21.66:443"
    secret = "ZWFmM2Q2NGNmNGM1NDIxMDljOWI2MjYwMWExNzhkNGI2N".encode()
    api_key = "ZDEzODNiOGM3ZGNmNGJjN2JjOTA1YjkxNTVhNzY4ZGE2O"

    authobj_dict = {
        'api_key': api_key,
        'upn': 'gateone',
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(secret,digestmod=hashlib.sha1)
    update_data = authobj_dict['api_key'] +authobj_dict['upn'] + authobj_dict['timestamp']
    my_hash.update(update_data.encode())
    authobj_dict['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url":gateone_server,"auth":authobj_dict}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)