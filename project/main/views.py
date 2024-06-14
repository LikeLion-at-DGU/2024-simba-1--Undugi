from django.shortcuts import render, redirect
from .models import Building, Route, Path

# Create your views here.
# def mainpage(request):
#    return render(request, 'main/mainpage.html')


def mainpage(request):
    if request.method == 'POST':
        start_building_id = request.POST.get('start_building')
        end_building_id = request.POST.get('end_building')
        calorie = request.POST.get('calorie')
        path_id = request.POST.get('path')
        
        # 경로 및 기타 데이터를 저장하거나 처리하는 로직 추가한 것
        start_building = Building.objects.get(id=start_building_id)
        end_building = Building.objects.get(id=end_building_id)
        path = Path.objects.get(id=path_id)
        
        Route.objects.create(
            start_building=start_building,
            end_building=end_building,
            path=path,
            calorie=calorie,
        )
        return redirect('map_page')

    buildings = Building.objects.all()
    paths = Path.objects.all()
    return render(request, 'main/mainpage.html', {'buildings': buildings, 'paths': paths})

def map_page(request):
    # 지도로 이동하는 로직 추가한 것
    routes = Route.objects.all()

    return render(request, 'map_page.html',{'routes': routes})
