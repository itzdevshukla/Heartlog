from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
def wellness(request):
    return render(request,"home/wellness.html")
def your_diary(request):
    return render (request,"home/yourdiary.html")
def guided_journaling(request):
    return render (request,"home/guided.html")
