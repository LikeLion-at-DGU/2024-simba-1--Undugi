from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Building, Visit
from ranking.models import Ranking
from accounts.models import Profile
import logging
def update_rankings():
    # 랭킹 업데이트 로직
    rankings = Ranking.objects.order_by('-total_calories_burned')
    for index, ranking in enumerate(rankings, start=1):
        ranking.rank = index
        ranking.save()


def mainpage(request):
    if request.method == 'POST':
        start_building_id = request.POST.get('start_building')
        end_building_id = request.POST.get('end_building')


        print("POST data received - Start:", start_building_id, "End:", end_building_id)

        # 폼 데이터가 없는 경우 예외 처리
        if not start_building_id or not end_building_id:
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'error': '모든 필드를 채워주세요!'
            })

        try:
            start_building = Building.objects.get(id=start_building_id)
            end_building = Building.objects.get(id=end_building_id)
        except ObjectDoesNotExist:
            print("Error: Building does not exist")
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'error': '유효하지 않은 데이터입니다!'
            })

        try:
            # 특정 경로에 대한 소모 칼로리를 설정합니다. (각주로 나타내야 할 부분)
            # 실제 칼로리 데이터는 나중에 입력해야 합니다.
            # 여기서는 임시로 100 kcal로 설정합니다.
            calorie_consumption = 100.0

            # Visit 객체 생성 및 저장
            new_visit = Visit.objects.create(
                start_building=start_building,
                end_building=end_building,
                calorie=calorie_consumption
            )

            print("Visit created successfully:", new_visit)  # 디버깅 메시지 추가

            # 맵 페이지로 데이터 전달
            return render(request, 'main/map.html', {
                'start_building': start_building,
                'end_building': end_building,
                'calorie_consumption': calorie_consumption
            })
        except Exception as e:
            print("Error creating Visit:", e)  # 디버깅 메시지 추가
            return render(request, 'main/mainpage.html', {
                'buildings': Building.objects.all(),
                'error': f'오류가 발생했습니다: {str(e)}'
            })


    buildings = Building.objects.all()
    return render(request, 'main/mainpage.html', {'buildings': buildings})


def map_page(request):
    if request.method == 'POST':
        start_building = request.POST.get('start_building', '')
        end_building = request.POST.get('end_building', '')

        try:
            start_building = Building.objects.get(name=start_building)
            end_building = Building.objects.get(name=end_building)
            visit = Visit.objects.get(start_building=start_building, end_building=end_building)
            calorie_consumption = visit.calorie
        except ObjectDoesNotExist:
             return render(request, 'main/map.html', {
                'error': '경로 데이터를 찾을 수 없습니다!'
            })
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            profile.consumedCalorie += calorie_consumption
            profile.save()

            try:
                user_ranking = Ranking.objects.get(nickname=request.user.username)
                user_ranking.total_calories_burned = profile.consumedCalorie
                user_ranking.save()
            except Ranking.DoesNotExist:
                user_ranking = Ranking.objects.create(
                    nickname=request.user.username,
                    total_calories_burned=profile.consumedCalorie
                )

            update_rankings()

            user_ranking = Ranking.objects.get(nickname=request.user.username)
            goal_calories = profile.goal
        else:
            user_ranking = None
            goal_calories = None

        remaining_calories = goal_calories - calorie_consumption if goal_calories else None

        return render(request, 'main/arrive.html', {
            'calorie_consumption': calorie_consumption,
            'user_ranking': user_ranking,
            'goal_calories': goal_calories
        })

    return redirect('main:mainpage')
        


    # 지도로 이동하는 로직 추가한 것
    #routes = Route.objects.all()

    #return render(request, 'map_page.html',{'routes': routes})
    #return render(request, 'main/map.html') # 개발 시 테스트용

def arrive(request):
    return render(request, 'main/arrive.html')