# Generated by Django 3.1.7 on 2021-04-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('survey_start_date', models.DateTimeField()),
            ],
        ),
    ]