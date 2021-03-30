# Generated by Django 3.1.1 on 2021-03-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
                ('phonenumber', models.IntegerField(default=0)),
                ('job', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]
