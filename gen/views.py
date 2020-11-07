from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return HttpResponse('<h5>About page</h5>')

def profile(request):
    return render(request,'generator/pp.html')

def password(request):

    p = ''
    c = list('asdfghjklzxcvbnmqwertyuiop')

    if request.GET.get('uc'):
        c.extend(list('ASDFGHJKLZXCVBNMQWERTYUIOP'))
    if request.GET.get('n'):
        c.extend(list('123456789'))
    if request.GET.get('sc'):
        c.extend("!@#$%^&*()~`:><?{}[]';./,")
    l = int(request.GET.get('length','3'))

    for x in range(l):
        p += random.choice(c)


    return render(request,'generator/password.html', {'p':p})

