from django.shortcuts import render,HttpResponse

# Create your views here.
def helloword(request):
    return HttpResponse("<H1>Holl Word,This is my First Django Web </H1>"
                        "<H2>I Love Pytho and Django, It's My Life </H2>")

def firspage (request):
    return render(request, 'firspage.html')

def secondpage (request):
    return render(request, 'secondpage.html')

def therdpage (request):
    return render(request, 'thirdpage.html')

def hnypage(request):
    return render(request,'hnypage.html')


def Home(request):
    return render(request,'Home.html')





