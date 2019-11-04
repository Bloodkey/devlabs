from django.shortcuts import render
from django.http import JsonResponse
import platform
from datetime import datetime



def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    date_now = datetime.now()
    date = date_now.strftime("%Y-%m-%d %H:%M:%S")
    page = request.path
    client = request.META['HTTP_USER_AGENT']
    response = {'date': date,
                'current_page': page,
                'server_info': {
                    'System': platform.system(),
                    'Release': platform.release(),
                    'Type': platform.machine(),
                },
                'client_info': client}
    return JsonResponse(response)
