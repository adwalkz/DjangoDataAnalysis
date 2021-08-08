# Generated by Django 3.1 on 2021-06-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='client_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='id',
        ),
        migrations.AddField(
            model_name='clients',
            name='company_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]