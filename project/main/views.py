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
        
         # 경로 추천 로직 예시: 일단 간단하게 최소 칼로리 경로를 선택하는 예시
        recommended_path = Path.objects.filter(calorie__lte=calorie).order_by('calorie').first()
        
        Route.objects.create(
            start_building=start_building,
            end_building=end_building,
            path=path,
            calorie=calorie,
        )
        
        
        # 사용자에게 적립되는 칼로리를 추가하는 로직은 여기에 추가
        # 예를 들어, 사용자 프로필에 적립된 칼로리를 저장하는 방식으로 구현
        # 이 부분은 사용자 모델이나 사용자 프로필 모델에 맞게 적용
        
        
        
        return redirect('map_page')

    buildings = Building.objects.all()
    paths = Path.objects.all()
    return render(request, 'main/mainpage.html', {'buildings': buildings, 'paths': paths})

def map_page(request):
    # 지도로 이동하는 로직 추가한 것
    routes = Route.objects.all()

    return render(request, 'map.html',{'routes': routes})
