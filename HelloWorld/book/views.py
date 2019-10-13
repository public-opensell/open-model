from django.shortcuts import render,render_to_response, redirect
from django.http import JsonResponse
from book.models import book
from book.models import user#导入models中user表
import json
from django.http.response import HttpResponse
from django.core import serializers
import requests
headers={     
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
def insert(request):#添加方法并展示
    content={}
    books=book.objects.all()           
    name=request.POST.get("bookname")
    auther=request.POST.get("bookauther") 
    prices=request.POST.get("bookprices")
    if name=="" or auther=="" or prices=="":
        content['oop']="数据不能为空！！！"
        return render(request,'shuju.html',content)        
    b=book(bname=name,bauther=auther,bprices=prices)
    b.save()
    return redirect("/login_user")
def truncate(req):#删除并重新排序
    bids=req.GET['id']#获取WSGIRequest对象id的值
    print(bids)
    b=book.objects.get(bid=bids)
    b.delete()
    return redirect("/login_user")
def update(req):#更新
    set={"status":True}
    bid=req.POST.get('bid')
    bname=req.POST.get('bname')
    bauther=req.POST.get('bauther')
    bprices=req.POST.get('bprices')
    b=book.objects.get(bid=bid)
    b.bname=bname
    b.bauther=bauther
    b.bprices=bprices
    b.save()
    return HttpResponse(json.dumps(set))
def login_user(request):#管理员登录
    content={}
    books=book.objects.all()
    s=0
    for i in books:
        pr=i.bprices 
        s+=pr
    if s==0 or pr==0:
        return render(request,"shuju.html",{"kings":"数据为空"})
            
    p=s/len(books)
    users=user.objects.all() 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
                   
        for indexs in users:
            t_type=indexs.typeword
            if username==indexs.username and password==indexs.password:
                return render(request,'shuju.html',{'wget':t_type,'user_list':books,"toal":s,"pj":p})               
            else:        
                content['message']="用户名和密码错误"
                return render(request,'login.html',content) 
    else:        
        for indexs in users:           
            t_type=indexs.typeword
        return render(request,'shuju.html',{'wget':t_type,'user_list':books,"toal":s,"pj":p}) 
def jinru(re): 
    return render(re, 'login.html')  

def test(request):
    
    poi=json.loads(request.body)#request.body获取前台携带的data数据并转化为json数据
        
    if request.method=="POST":
        username=poi['username']
        password=poi['password']
        print(username,password)
        users=user.objects.all()     
        for indexs in users:
            t_type=indexs.typeword
            if username==indexs.username and password==indexs.password:
               return render_to_response("index.html")               
            else:        
               return render_to_response("error.html") 
   
      
def get(res):  
    bnames=res.POST.get("bookname")
    print(bnames)
    book_names=book.objects.filter(bname__contains=bnames)#__contains模糊查询   
    queryset=serializers.serialize("json", book_names)#在Django框架中，我们不能直接将QuerySet对象通过 HttpResponse(json.dumps(QeurySet))返回给前端Ajax....#否则会报错：Object of type 'QuerySet' is not JSON serializable
    return HttpResponse(json.dumps(queryset))
def qqmusic(res):
    name_list=[]
    singer_name=res.POST.get("namesearch")
    print(singer_name)
    name_path="https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&lossless=0&flag_qc=0&p=1&n=66&w={}".format(singer_name)
    url_html=requests.get(name_path,headers=headers)
    text_name=url_html.content.decode()#获得text文本
    text_list=text_name[9:len(text_name)-1]
    json_name=json.loads(text_list)#将字符窜转化为json数据
    for name in json_name["data"]["song"]["list"]:
        jio=name["songname"]        
        lists=name["songmid"]#获取songmid
        two_path="https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&cid=205361747&songmid=%s&filename=C400%s.m4a&guid=2445378780"%(lists,lists)
        url_htmls=requests.get(two_path,headers=headers)
        text_names=url_htmls.content.decode()#获得text文本   
        json_names=json.loads(text_names)
        for fttp in json_names["data"]["items"]:
            vkey=fttp["vkey"]#获取vkey的值
            down_path="http://dl.stream.qqmusic.qq.com/C400%s.m4a?vkey=%s&guid=2445378780&uin=0&fromtag=66"%(lists,vkey)
            lop_url={"name":jio,"url_path":down_path}
            name_list.append(lop_url)
    return HttpResponse(json.dumps(name_list))
    