# Generated by Django 3.1 on 2021-06-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0008_surveyquestion_surveyquestionchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='ques_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
