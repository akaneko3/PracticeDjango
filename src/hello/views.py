from django.shortcuts import render, render_to_response

# Create your views here.
def index(request, my_name='django'):
    page_title = 'Hello page'
    return render_to_response('hello/hello.djhtml', locals())
