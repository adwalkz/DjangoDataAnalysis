from django.db import models

class Clients(models.Model):
    company_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    survey_start_date = models.DateTimeField()
    status = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Clients"
    

    def __str__(self):
        return self.client_name

