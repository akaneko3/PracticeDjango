from django.shortcuts import render, render_to_response

# Create your views here.
def index(request, my_name):
    return render_to_response('hello/hello.djhtml', {
        'page_title': 'Hello page',
        'my_name': my_name,
    })
