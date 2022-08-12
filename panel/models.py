from django.db import models


class Server(models.Model):
    server_id = models.BigAutoField(primary_key=True)
    server_name = models.CharField(default='server_name',max_length=200)
    cpu_usage = models.CharField(max_length=5)
    mem_usage = models.CharField(max_length=5)
    load_avg = models.CharField(max_length=20)
    uptime_day = models.IntegerField()
    uptime_hour = models.IntegerField()
    uptime_minute = models.IntegerField()
    uptime_second = models.IntegerField()
    Last_Update = models.DateTimeField('last update',auto_now=True)
    def __str__(self):
        return self.server_name
