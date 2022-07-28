from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')

def colorResult(request):
        ColorRed = int(request.GET['1']) + int(request.GET['2'])
        ColorGreen = int(request.GET['3']) + int(request.GET['4'])
        ColorBlue = int(request.GET['5']) + int(request.GET['6'])
        
        data = {}

        if((ColorRed >= 6) and (ColorGreen < 6) and (ColorBlue < 6 )):
             data['data']= 1

        elif((ColorRed >= 6) and (ColorGreen >= 6) and (ColorBlue < 6 )):
             data['data']= 2
        
        elif((ColorRed >= 6) and (ColorGreen < 6) and (ColorBlue >= 6 )):
             data['data']= 3

        elif((ColorRed < 6) and (ColorGreen < 6) and (ColorBlue >= 6 )):
             data['data']= 4
        
        elif((ColorRed < 6) and (ColorGreen >= 6) and (ColorBlue >= 6 )):
             data['data']= 5

        elif((ColorRed < 6) and (ColorGreen >= 6) and (ColorBlue < 6 )):
             data['data']= 6

        elif((ColorRed >= 6) and (ColorGreen >= 6) and (ColorBlue >= 6 )):
             data['data']= 7

        elif((ColorRed < 6) and (ColorGreen < 6) and (ColorBlue < 6 )):
             data['data']= 7

        return JsonResponse(data, status=200)


# red 1 green 0 blue 0 => 1(가온누리)
# red 1 green 1 blue 0 => 2(라온제나)
# red 1 green 0 blue 1 => 3(두빛나래)
# red 0 green 0 blue 1 => 4(가람)
# red 0 green 1 blue 1 => 5(미르)
# red 0 green 1 blue 0 => 6(온새미로)
# red 1 green 1 blue 1 => 7(꽃구름)
# red 0 green 0 blue 0 => 8(가온길)
