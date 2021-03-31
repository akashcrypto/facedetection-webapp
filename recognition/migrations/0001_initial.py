# Generated by Django 3.1.1 on 2021-03-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('inTime', models.DateTimeField(blank=True, null=True)),
                ('outTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CameraMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(blank=True, null=True)),
                ('browserUniqueName', models.CharField(blank=True, max_length=100, null=True)),
                ('isNeedToStopCamera', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recognition',
            fields=[
                ('sId', models.IntegerField(primary_key=True, serialize=False)),
                ('requestTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=20, null=True)),
                ('lname', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('cls', models.CharField(blank=True, max_length=20, null=True)),
                ('residence', models.CharField(blank=True, max_length=50, null=True)),
                ('fathername', models.CharField(blank=True, max_length=20, null=True)),
                ('contact', models.IntegerField(default=0)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('totalAttendance', models.IntegerField(default=0)),
            ],
        ),
    ]
