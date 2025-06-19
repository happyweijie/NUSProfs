from django.shortcuts import render

def search_demo(request):
    return render(request, "api/demo.html")
