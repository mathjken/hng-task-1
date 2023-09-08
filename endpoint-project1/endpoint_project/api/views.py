from django.shortcuts import render

# Create your views here.
# api/views.py
from django.http import JsonResponse
from .models import ApiResponse
import datetime

def get_info(request):
    slack_name = request.GET.get('slack_name', 'Johnkennedy')
    track = request.GET.get('track', 'backend')
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow()

    # Save the data to the database (you can adjust this based on your needs)
    ApiResponse.objects.create(
        slack_name="Johnkennedy",
        current_day=current_day,
        utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        track="backend",
        github_file_url="https://github.com/mathjken/hng-task-1/tree/main/endpoint-project/",
        github_repo_url="https://github.com/mathjken/hng-task-1",
    )

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/mathjken/hng-task-1/tree/main/endpoint-project",
        "github_repo_url": "https://github.com/mathjken/hng-task-1",
        "status_code": 200
    }

    return JsonResponse(response_data)

