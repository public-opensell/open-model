import requests
import os

headers={
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    }
pvideo=os.getcwd()+"\pvideo"
def hight():    
    if not os.path.exists(pvideo):    
        os.mkdir(pvideo)
    lou="000"
    i=256
    while True:    
        i+=1
        if  i==100 or len(lou+str(i))>5:        
            louss=lou[:2]+str(i)
            htmls="https://cn3.ruioushang.com/hls/20190407/d137a20da78f708c078086fcf2384287/1554640507/film_{}.ts".format(louss)
            htmls_content=requests.get(htmls,headers=headers)
            with open(pvideo+"/{}.ts".format(i),"wb") as f:
                f.write(htmls_content.content)
                print("第{}个下载成功".format(i))
            if i==300:
                break
        else:
            lous=lou+str(i)        
            htmls="https://cn3.ruioushang.com/hls/20190407/d137a20da78f708c078086fcf2384287/1554640507/film_{}.ts".format(lous)
            htmls_content=requests.get(htmls,headers=headers)
            with open(pvideo+"/{}.ts".format(i),"wb") as f:
                f.write(htmls_content.content)
                print("第{}个下载成功".format(i))
            if i==300:
                break
    writevideo()
def writevideo():
    for i,j,kin in os.walk(pvideo):#获取文件夹下的所有文件名
        for jkl in kin:
            file=open(pvideo+"/filelist.txt",'a')#'w'覆盖原文件  'a'后面进行追加
            file.write("file '{}'".format(jkl)+'\n')#'\n'换行符   将字符串  file '文件名'.txt 写入filelist文档中
    toalvideo()
def toalvideo():
    os.chdir(pvideo)
    os.system("cmd/c ffmpeg -f concat -i filelist.txt -c copy VideoOutput.mp4 ")#cmd/c 执行完之后关闭cmd窗口  cmd /k执行完不关闭cmd窗口
    
if __name__=="__main__":
    hight()



