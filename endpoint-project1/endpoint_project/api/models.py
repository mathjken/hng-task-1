from django.db import models

class ApiResponse(models.Model):
    slack_name = models.CharField(max_length=255)
    current_day = models.CharField(max_length=20)
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=20)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()

