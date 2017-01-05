from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    page_title = 'Hello page'
    my_name = 'Jun'
    return render_to_response('hello/hello.djhtml', locals())
