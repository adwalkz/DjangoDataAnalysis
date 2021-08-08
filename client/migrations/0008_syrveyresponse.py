# Generated by Django 3.1 on 2021-07-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0012_auto_20210701_1820'),
        ('client', '0007_auto_20210710_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyrveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_response', models.CharField(max_length=255)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ts.clients')),
                ('ques_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.surveyquestion')),
            ],
        ),
    ]
