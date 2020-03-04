# Generated by Django 3.0.3 on 2020-03-04 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(unique=True)),
                ('round', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('visited_goals', models.IntegerField()),
                ('visited_goals_half_time', models.IntegerField()),
                ('visitors_goals', models.IntegerField()),
                ('visitors_goals_half_time', models.IntegerField()),
                ('externalFileName', models.CharField(max_length=150)),
                ('visited_shots', models.IntegerField()),
                ('visitors_shots', models.IntegerField()),
                ('date', models.DateField()),
                ('swag', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(unique=True)),
                ('sport', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('currentSeason', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chancePyApp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chancePyApp.Country')),
                ('leagues', models.ManyToManyField(to='chancePyApp.League')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chancePyApp.Country')),
                ('played_at', models.ManyToManyField(to='chancePyApp.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Odd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=25)),
                ('value', models.FloatField()),
                ('won', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chancePyApp.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='chancePyApp.League'),
        ),
        migrations.AddField(
            model_name='game',
            name='visited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visited', to='chancePyApp.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='visited_players',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visited_players', to='chancePyApp.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='visitors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to='chancePyApp.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='visitors_players',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors_players', to='chancePyApp.Player'),
        ),
    ]
