# Generated by Django 3.1 on 2021-07-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_surveyquestion_ques_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='ques_type',
            field=models.IntegerField(choices=[(1, 'TEXT'), (2, 'CHOICE')], default=1),
        ),
    ]
