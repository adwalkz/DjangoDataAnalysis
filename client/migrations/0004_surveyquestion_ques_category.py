# Generated by Django 3.1 on 2021-07-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20210708_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='ques_category',
            field=models.CharField(default='GENERAL', max_length=255),
        ),
    ]
