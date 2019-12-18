# Generated by Django 3.0 on 2019-12-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('Longtitude', models.FloatField()),
                ('Address', models.TextField(max_length=100)),
                ('rate', models.SmallIntegerField()),
            ],
        ),
    ]
