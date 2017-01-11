from django.shortcuts import render, render_to_response, get_object_or_404
from majorcity.models import City

# Create your views here.
def index(request):
    cities = City.objects.all()
    return render_to_response('majorcity/list.djhtml', {
        'cities': cities,
        'page_title': '日本の政令指定都市',
        'css_file': 'majorcity/css/list.css'
    })

def show(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render_to_response('majorcity/detail.djhtml', {
        'city': city,
        'page_title': f'{city.name}の詳細',
        'css_file': 'majorcity/css/detail.css'
    })
