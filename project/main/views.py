from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Building, Route, Path

def mainpage(request):
    if request.method == 'POST':
        start_building_id = request.POST.get('start_building')
        end_building_id = request.POST.get('end_building')
        path_id = request.POST.get('path')

        # 폼 데이터가 없는 경우 예외 처리
        if not start_building_id or not end_building_id or not path_id:
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'paths': Path.objects.all(),
                'error': '모든 필드를 채워주세요!'
            })

        try:
            start_building = Building.objects.get(id=start_building_id)
            end_building = Building.objects.get(id=end_building_id)
            path = Path.objects.get(id=path_id)
        except ObjectDoesNotExist:
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'paths': Path.objects.all(),
                'error': '유효하지 않은 데이터입니다!'
            })

        try:
            Route.objects.create(
                start_building=start_building,
                end_building=end_building,
                path=path
            )

            return redirect('map_page')
        except Exception as e:
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'paths': Path.objects.all(),
                'error': f'오류가 발생했습니다: {str(e)}'
            })

    buildings = Building.objects.all()
    paths = Path.objects.all()
    return render(request, 'main/mainpage.html', {'buildings': buildings, 'paths': paths})

def map_page(request):
    # Logic for displaying the map page
    return render(request, 'main/map.html')
