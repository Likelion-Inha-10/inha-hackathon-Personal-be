from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')

def musicResult(request):
        MusicRed = int(request.GET['1']) + int(request.GET['2'])
        MusicGreen = int(request.GET['3']) + int(request.GET['4'])
        MusicBlue = int(request.GET['5']) + int(request.GET['6'])
        
        data = {}

        if((MusicRed < 6) and (MusicGreen < 6) and (MusicBlue < 6 )):
             data['data']= 1

        elif((MusicRed < 6) and (MusicGreen < 6) and (MusicBlue >= 6 )):
             data['data']= 6
        
        elif((MusicRed < 6) and (MusicGreen >= 6) and (MusicBlue < 6 )):
             data['data']= 5

        elif((MusicRed < 6) and (MusicGreen >= 6) and (MusicBlue >= 6 )):
             data['data']= 2
        
        elif((MusicRed >= 6) and (MusicGreen < 6) and (MusicBlue < 6 )):
             data['data']= 3

        elif((MusicRed >= 6) and (MusicGreen < 6) and (MusicBlue >= 6 )):
             data['data']= 8

        elif((MusicRed >= 6) and (MusicGreen >= 6) and (MusicBlue < 6 )):
             data['data']= 7

        elif((MusicRed >= 6) and (MusicGreen >= 6) and (MusicBlue >= 6 )):
             data['data']= 4

        return JsonResponse(data, status=200)

# red 0 green 0 blue 0 => 1(바순)
# red 0 green 1 blue 1 => 2(첼로)
# red 1 green 0 blue 0 => 3(마림바)
# red 1 green 1 blue 1 => 4(오보에)
# red 0 green 1 blue 0 => 5(파이프 오르간)
# red 0 green 0 blue 1 => 6(피아노)
# red 1 green 1 blue 0 => 7(팀파니)
# red 1 green 0 blue 1 => 8(바이올린)

