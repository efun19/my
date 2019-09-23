from django.shortcuts import render
from userApp import models

# Create your views here.
#主页面
def indexPage(req):
    return render(req,'index.html')
#注册页面
def regist(req):
    #1往usesrinfo表单插入表单
    #2 获取form表单提交的数据
    if req.method=="POST":
        usname=req.POST.get("uname")
        uspsw=req.POST.get("psw")
        #验证用户名是否被注册
        # filter返回记录数0或者1
        # get返回记录数 必须为1 否则报错
        obj=models.Userinfo.objects.filter(username=usname)
        if obj:
            return render(req,"register.html", {"msg":"注册失败，用户名已被注册"})
        else:
            #新增
            user=models.Userinfo(
                username=usname,
                userpassword=uspsw,
            )
            user.save()
            return render(req,"register.html",{"msg":"注册成功","msg3":"请登录"})
    else:
        return render(req,"register.html")
#登录页面
def login(req):
    if req.method == "POST":
        #获取用户信息
        usname = req.POST.get("uname")
        uspsw = req.POST.get("psw")
        #验证用户名密码正确性
        obj=models.Userinfo.objects.filter(username=usname,userpassword=uspsw).first()
        if obj:
            #登录成功 保存用户登录状态 供多个页面获取与验证 session或者cookie
            req.session["user"]=obj
            req.session.set_expiry(0) #过期时间半小时
            return  render(req,"index.html")
            #return render(req, "login.html",{"msg":"登录成功","msg2":"返回主页面"})
        else:
            #登录失败
            return render(req,"login.html",{"msg":"登录失败 用户名或密码错误"})
    else:
        return render(req,"login.html")
#退出页面
def logout(req):
    req.session.flush()
    return render(req, 'index.html')

def tuPage(req):
    return render(req,'showphoto.html')

def shaixuan(req):
    return render(req,'shaixuan.html')


