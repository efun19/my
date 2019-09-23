from infomodle import models
from django.shortcuts import render
import pymysql
import  requests
from  bs4 import  BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib as mp
from django.db.models import Q
# Create your views here.
#爬虫函数
def getInfo(req):
    if req.session.get("user"):
        #爬取
        deleteinfo()
        con = pymysql.connect("localhost", 'root', 'root', 'Mydb');
        db = con.cursor()
        for i in range(1, 16):
            url = "http://hrb.ganji.com/ershoufang/pn{}/".format(i)
            f = requests.get(url).text
            soup = BeautifulSoup(f, "html.parser")
            divlist = soup.find_all(class_="f-list-item ershoufang-list")
            for div in divlist:
                housename = div.find(class_="js-title value title-font").get_text();
                houseadd = div.find("a", attrs={"class": "address-eara"}).get_text()
                addname = div.find("span", attrs={"class": "address-eara"}).get_text()
                price = div.find("span", attrs={"class": "num"}).get_text()
                xx = div.find(class_="dd-item size").get_text();
                xx = xx.split()
                housetype = xx[0]
                housearea = xx[1].split("㎡")[0]
                housebound = xx[2]
                housefloor = xx[3]
                price = float(price)
                housearea = float(housearea)
                if price <= 50:
                    pricerange = "50万以下"
                elif 50 < price <= 100:
                    pricerange = "50万-100万"
                elif 100 < price <= 150:
                    pricerange = "100万-150万"
                elif 150 < price <= 200:
                    pricerange = "150万-200万"
                else:
                    pricerange = "200万以上"
                if housearea <= 50:
                    arearange = "50平米以下"
                elif 50 < housearea <= 80:
                    arearange = "50平米-80平米"
                elif 80 < housearea <= 110:
                    arearange = "80平米-110平米"
                elif 110 < housearea <= 140:
                    arearange = "110平米-140平米"
                else:
                    arearange = "140平米以上"
                sql = "insert into houseinfo(housename,houseadd,addname,price,housetype,housearea,housebound,housefloor,pricerange,arearange) values('%s','%s','%s','%f','%s','%f','%s','%s','%s','%s')" % (
                housename, houseadd, addname, price, housetype, housearea, housebound, housefloor, pricerange,
                arearange)
                db.execute(sql)
                con.commit()
        db.close()
        con.close()
        return render(req,"index2.html")
    else:
        return render(req,"login.html")

def delete(req):
    deleteinfo()
    return render(req,"index.html",{"msg":"2"})

def deleteinfo():
    con = pymysql.connect("localhost", 'root', 'root', 'Mydb');
    db = con.cursor()
    sql = "DELETE  FROM houseinfo WHERE 1=1"
    db.execute(sql)
    con.commit()

#展示
def index2Page(req):
    if req.session.get("user"):
        if models.Houseinfo.objects.first():
            return render(req,"index2.html")
        else:
            return render(req,"index.html", {"msg": "1"})
    else:
        return render(req,"login.html")
#显示全部信息
def list(req):
    if req.session.get("user"):
        housercount=models.Houseinfo.objects.count()
        housers_list = models.Houseinfo.objects.all()
        return render(req,'showall.html', {"housers":housers_list,"msg":housercount})
    else:
        return render(req,"login.html")

def houseadd():
    com = create_engine("mysql+pymysql://root:root@localhost:3306/mydb")
    sql = "select houseadd,count(houseadd) as sumadd  from houseinfo  GROUP BY houseadd having count(houseadd)>10"
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"
    mp.rcParams["font.size"] = 10
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=80)
    x = df["houseadd"]
    y = df["sumadd"]
    plt.plot(x, y)
    plt.xlabel("区域")
    plt.ylabel("数量")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.title("哈尔滨二手房区域数量折线图")
    plt.grid()
    plt.savefig("static/images/thumbs/add1.png")
    plt.figure()
    plt.bar(x, y, color="b", alpha=0.5)
    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 7, y, ha="center", va="top")
    plt.xlabel("区域")
    plt.ylabel("数量")
    plt.title("哈尔滨二手房区域数量柱状图")
    plt.savefig("static/images/thumbs/add2.png")
    plt.figure()
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=120)
    labels = df["houseadd"]
    facs = df["sumadd"]
    temp = zip(facs, labels)
    plt.pie(x=facs, labels=labels, labeldistance=1.1, pctdistance=0.6, startangle=90, autopct='%.2f%%')
    plt.legend(loc=0)
    plt.title("哈尔滨二手房区域数量饼状图")
    plt.savefig("static/images/thumbs/add3.png")

def housetype():
    com = create_engine("mysql+pymysql://root:root@localhost:3306/mydb")
    sql = "select housetype,count(housetype) as sumtype  from houseinfo  GROUP BY housetype HAVING count(housetype)>10"
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"
    mp.rcParams["font.size"] = 10
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=80)
    x = df["housetype"]
    y = df["sumtype"]
    plt.plot(x, y)
    plt.xlabel("户型")
    plt.ylabel("数量")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.title("哈尔滨二手房户型折线图")
    plt.grid()
    plt.savefig("static/images/thumbs/type1.png")
    plt.figure()
    plt.bar(x, y, color="b", alpha=0.5)
    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 7, y, ha="center", va="top")
    plt.xlabel("户型")
    plt.ylabel("数量")
    plt.title("哈尔滨二手房户型柱状图")
    plt.savefig("static/images/thumbs/type2.png")
    plt.figure()
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=120)
    labels = df["housetype"]
    facs = df["sumtype"]
    temp = zip(facs, labels)
    plt.pie(x=facs, labels=labels, labeldistance=1.1, pctdistance=0.6, startangle=90, autopct='%.2f%%')
    plt.legend(loc=0)
    plt.title("哈尔滨二手房户型饼状图")
    plt.savefig("static/images/thumbs/type3.png")

def houseprice():
    com = create_engine("mysql+pymysql://root:root@localhost:3306/mydb")
    sql = "select pricerange,count(pricerange) as sumprice  from houseinfo  GROUP BY pricerange"
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"
    mp.rcParams["font.size"] = 10
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=80)
    x = df["pricerange"]
    y = df["sumprice"]
    plt.plot(x, y)
    plt.xlabel("房价")
    plt.ylabel("数量")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.title("哈尔滨二手房房价折线图")
    plt.grid()
    plt.savefig("static/images/thumbs/price1.png")
    plt.figure()
    plt.xlabel("房价")
    plt.ylabel("数量")
    plt.bar(x, y, color="b", alpha=0.5)
    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 7, y, ha="center", va="top")
    plt.title("哈尔滨二手房房价柱状图")
    plt.savefig("static/images/thumbs/price2.png")
    plt.figure()
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=120)
    labels = df["pricerange"]
    facs = df["sumprice"]
    temp = zip(facs, labels)
    plt.pie(x=facs, labels=labels, labeldistance=1.1, pctdistance=0.6, startangle=90, autopct='%.2f%%')
    plt.legend(loc=0)
    plt.title("哈尔滨二手房房价饼状图")
    plt.savefig("static/images/thumbs/price3.png")


def housearea():
    com = create_engine("mysql+pymysql://root:root@localhost:3306/mydb")
    sql = "select arearange,count(arearange) as sumarea  from houseinfo  GROUP BY arearange"
    df = pd.read_sql_query(sql, com)
    mp.rcParams["font.family"] = "Microsoft YaHei"
    mp.rcParams["font.size"] = 10
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=80)
    x = df["arearange"]
    y = df["sumarea"]
    plt.plot(x, y)
    plt.xlabel("面积")
    plt.ylabel("数量")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.title("哈尔滨二手房面积折线图")
    plt.grid()
    plt.savefig("static/images/thumbs/area1.png")
    plt.figure()
    plt.xlabel("面积")
    plt.ylabel("数量")
    plt.bar(x, y, color="b", alpha=0.5)
    temp = zip(x, y)
    for x, y in temp:
        plt.text(x, y + 7, y, ha="center", va="top")
    plt.title("哈尔滨二手房面积柱状图")
    plt.savefig("static/images/thumbs/area2.png")
    plt.figure()
    plt.figure(figsize=(10, 8), facecolor="#F1F5FB", dpi=120)
    labels = df["arearange"]
    facs = df["sumarea"]
    temp = zip(facs, labels)
    plt.pie(x=facs, labels=labels, labeldistance=1.1, pctdistance=0.6, startangle=90, autopct='%.2f%%')
    plt.legend(loc=0)
    plt.title("哈尔滨二手房面积饼状图")
    plt.savefig("static/images/thumbs/area3.png")

def photo(req):
    if req.session.get("user"):
        houseadd()
        housetype()
        houseprice()
        housearea()
        return render(req,'index2.html',{"msg":"x"})
    else:
        return render(req,"login.html")

def qu(req):
    if req.session.get("user"):
        quyu=req.POST.get("quname")
        qianc=req.POST.get("qianname")
        mianc=req.POST.get("mianname")
        typec=req.POST.get("typename")
        boundc=req.POST.get("boundname")
        qu_list = models.Houseinfo.objects.filter(houseadd__contains=quyu,pricerange__startswith=qianc,arearange__startswith=mianc,housetype__contains=typec,housefloor__contains=boundc).all()
        housecount=models.Houseinfo.objects.filter(houseadd__contains=quyu,pricerange__startswith=qianc,arearange__startswith=mianc,housetype__contains=typec,housefloor__contains=boundc).count()
        return render(req, 'qu.html', {"qus":qu_list,"msg":housecount})
    else:
        return render(req,"login.html")