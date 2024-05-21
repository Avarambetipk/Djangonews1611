from django.shortcuts import render
import datetime

# Create your views here.
def wishh(request):
    time=datetime.datetime.now()
    name="sunny"
    cour="python"
    requir="python"
    my_dic={"time":time,"cour":cour,"requir":requir,"name":name}
    return render(request,"newapp/new.html",my_dic)

