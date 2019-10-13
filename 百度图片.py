import requests
import json
import os
import pymysql as py
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
def splider(world):
    path_html=os.getcwd()+"\picturesss"
    if not os.path.exists(path_html):
        os.mkdir(path_html)
    i=0
    
    while True:
        html_html="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word={}&z=0&ic=0&hd=undefined&latest=undefined&copyright=undefined&s=undefined&se=&tab=0&width=&height=&face=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=1429216642%2C2416737722&catename=&force=undefined&cardserver=&tabname=&pn={}&rn=10&gsm=&1569290685080=".format(world,i)     
        htmls=requests.get(html_html,headers=headers)
        html_htmls=htmls.content
        json_html=json.loads(html_htmls)
        for indexs in range (len(json_html['data'])-1):      
            uios=requests.get(json_html['data'][indexs]['hoverURL'],headers=headers)
            f=open(path_html+"/{}.".format(json_html['data'][indexs]['di'])+json_html['data'][indexs]['hoverURL'][-3:],"wb")
            f.write(uios.content)
            print(json_html['data'][indexs]['di']+"==下载成功")
            
        i+=10
        print(i)
def copyword():
    mysqldb=py.connect("localhost","root","123456","order_list")
    cursor=mysqldb.cursor()
    sqls="create table if not exists order_tbl(order_id int primary key auto_increment,order_name varchar(5000) not null unique,order_picture varchar(5500) not null unique)"#unique   mysql数据库唯一字段
    cursor.execute(sqls)
    sql="insert into order_tbl(order_name,order_picture) value ('%s','%s')"%(name,junk)
    try:
        cursor.execute(sql)       
        mysqldb.commit()
    except :
        mysqldb.rollback()
        print("数据插入失败")
    cursor.close()
    mysqldb.close()     
if __name__=="__main__":
    iops=input("请输入要下载的图片：")
    splider(iops)
