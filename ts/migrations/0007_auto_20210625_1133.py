# Generated by Django 3.1 on 2021-06-25 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0006_auto_20210625_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='name',
            new_name='client_name',
        ),
    ]
