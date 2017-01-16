from django.shortcuts import render, get_object_or_404
from major_city.models import City

# Create your views here.
def index(request):
    cities = City.objects.all()
    return render(request, 'major_city/list.djhtml', {
        'cities': cities,
        'page_title': '日本の政令指定都市',
        'css_file': 'major_city/css/list.css'
    })


def show(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'major_city/detail.djhtml', {
        'city': city,
        'page_title': f'{city.name}の詳細',
        'css_file': 'major_city/css/detail.css'
    })
