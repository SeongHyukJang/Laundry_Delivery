# Generated by Django 3.0 on 2019-12-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191211_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]