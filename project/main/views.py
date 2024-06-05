from django.shortcuts import render, redirect
from .models import Building, Route, Path

# Create your views here.
# def mainpage(request):
#    return render(request, 'main/mainpage.html')


def main_page(request):
    if request.method == 'POST':
        start_building_id = request.POST.get('start_building')
        end_building_id = request.POST.get('end_building')
        calorie = request.POST.get('calorie')
        path_id = request.POST.get('path')
        
        # 경로 및 기타 데이터를 저장하거나 처리하는 로직 추가
        return redirect('map_page')

    buildings = Building.objects.all()
    paths = Path.objects.all()
    return render(request, 'main_page.html', {'buildings': buildings, 'paths': paths})

def map_page(request):
    # 지도로 이동하는 로직 추가
    return render(request, 'map_page.html')
