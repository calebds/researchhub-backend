from django.db import models

class WebsiteVisits(models.Model):
    uuid = models.CharField(max_length=32, unique=True)
    saw_signup_banner = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.uuid}'