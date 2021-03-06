# Generated by Django 3.1 on 2021-07-01 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ts', '0012_auto_20210701_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('ques_id', models.AutoField(primary_key=True, serialize=False)),
                ('ques_type', models.IntegerField(default=0)),
                ('ques_text', models.CharField(max_length=255)),
                ('ques_meta_1', models.CharField(max_length=255)),
                ('ques_meta_2', models.CharField(max_length=255)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ts.clients')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ts.clients')),
                ('ques_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.surveyquestion')),
            ],
        ),
    ]
