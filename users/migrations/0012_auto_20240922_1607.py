# Generated by Django 3.1.8 on 2024-09-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]