# Generated by Django 3.2.4 on 2021-06-15 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heartbeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_recieved', models.DateTimeField(editable=False)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorheartbeat.sensor')),
            ],
        ),
    ]
