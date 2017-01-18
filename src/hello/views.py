from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

# Create your views here.
def hello(request):
    my_name = request.session['your_name']
    return render(request, 'hello/hello.djhtml', {
        'page_title': 'hello page',
        'my_name': my_name,
    })


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            request.session['your_name'] = your_name
            return HttpResponseRedirect('thanks/')
    else:
        form = NameForm()
    return render(request, 'hello/form.djhtml', {
        'page_title': 'name entry',
        'form': form,
    })
