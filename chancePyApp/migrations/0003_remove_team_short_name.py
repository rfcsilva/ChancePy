# Generated by Django 3.0.3 on 2020-03-03 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chancePyApp', '0002_auto_20200303_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='short_name',
        ),
    ]