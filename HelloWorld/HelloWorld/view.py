from django.shortcuts import render
import os
from django.http.response import HttpResponse
def html(req):
    return render(req, "hello.html")
    
def kugou(request):
   
    ip=request.META['REMOTE_ADDR']
    print(ip)
    content={}
    if request.method=="POST":
        myfile=request.FILES.get("files",None)
        #print(myfile.size/1048576)#myfile.size获取字节大小/1048576=M
        #print(myfile.name)获取文件名和后缀名
        if not myfile:
            content['successful']="无文件无法上传，请添加文件！！！"
            return render(request,'hello.html',content) 
        else:
            with open(os.path.join(os.getcwd(),myfile.name),'wb+') as file:
                for ind in myfile.chunks():
                    file.write(ind)
            content['success']="上传成功！！！！"
            return render(request, 'hello.html',content)
                    
        file.close()
    else:
        content['ind']="非法操作！！！！"
        return render(request,'hello.html',content)
                
                

        

            
            

        