# Generated by Django 3.1 on 2021-06-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0009_auto_20210625_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestionchoice',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ts.clients'),
        ),
    ]