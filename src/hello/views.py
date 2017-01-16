from django.shortcuts import render

# Create your views here.
def index(request, my_name='django'):
    page_title = 'Hello page'
    return render(request, 'hello/hello.djhtml', locals())
