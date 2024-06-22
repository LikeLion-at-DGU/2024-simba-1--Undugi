from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Building, Route, Path
from ranking.models import Ranking
from accounts.models import Profile
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
            # 경로에 해당하는 소모 칼로리 계산
            calorie_consumption = path.calorie

            # Route 객체 생성
            new_route = Route.objects.create(
                start_building=start_building,
                end_building=end_building,
                path=path,
                calorie=calorie_consumption
            )

             # 사용자 소모 칼로리 업데이트
            if request.user.is_authenticated:
                profile = Profile.objects.get(user=request.user)
                profile.consumedCalorie += calorie_consumption
                profile.save()

                # 랭킹 업데이트
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

                # 사용자 순위 조회
                user_ranking = Ranking.objects.get(nickname=request.user.username)

                # 목표 소모 칼로리 가져오기
                goal_calories = profile.goal

            else:
                user_ranking = None
                goal_calories = None

            # arrive.html로 데이터 전달
            return render(request, 'main/arrive.html', {
                'calorie_consumption': calorie_consumption,
                'user_ranking': user_ranking,
                'goal_calories': goal_calories
            })


            

           

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

    # 지도로 이동하는 로직 추가한 것
    #routes = Route.objects.all()

    #return render(request, 'map_page.html',{'routes': routes})
    return render(request, 'main/map.html') # 개발 시 테스트용

def arrive(request):
    return render(request, 'main/arrive.html')