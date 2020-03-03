# Generated by Django 3.0.3 on 2020-03-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancePyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='leagues',
            field=models.ManyToManyField(to='chancePyApp.League'),
        ),
        migrations.AddField(
            model_name='team',
            name='short_name',
            field=models.CharField(default='DEFAULT', max_length=10),
            preserve_default=False,
        ),
    ]
