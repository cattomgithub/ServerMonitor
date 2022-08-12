from django.db import models

class OSDetail (models.Model):
    Server_ID = models.CharField(max_length=5,primary_key=True)
    Uptime_Day = models.CharField(max_length=10)
    Uptime_Hour = models.CharField(max_length=10)
    Uptime_Min = models.CharField(max_length=10)
    Uptime_Sec = models.CharField(max_length=10)
    CPU_Usage = models.CharField(max_length=10)
    Memory_Usage = models.CharField(max_length=10)
    def __str__(self):
        return self.Server_ID