# Generated by Django 3.1 on 2021-06-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0005_auto_20210625_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='company_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
