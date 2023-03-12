from django.shortcuts import render
from Points.models import Post
from django.http import HttpResponse

def addm(request):
    err_msg=""
    val = Post.objects.first()
    rp = val.rp
    mp = val.mp
    if rp > 0:
        val.rp = rp - 1
        val.mp = mp + 1
        val.save()
        mp = val.mp
        rp = val.rp
    else:
        err_msg = 'Insufficient balance'

    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def addr(request):
    err_msg=""

    val = Post.objects.first()
    rp = val.rp
    mp = val.mp

    if mp > 0:
        val.mp = mp - 1
        val.rp = rp + 1
        val.save()
        mp = val.mp
        rp = val.rp
    else:
        err_msg = 'Insufficient balance'


    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def index(request):
    err_msg=""
    val = Post.objects.first()
    rp = val.rp
    mp = val.mp
    return render(request, 'index.html',{
    'rp':rp,
    'mp':mp,
    'err_msg':err_msg
    })