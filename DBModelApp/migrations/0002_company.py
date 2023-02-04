# Generated by Django 4.1.1 on 2023-01-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBModelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compid', models.IntegerField()),
                ('compname', models.CharField(max_length=60)),
                ('noofemps', models.IntegerField()),
                ('compaddr', models.CharField(max_length=50)),
                ('compshare', models.FloatField()),
            ],
        ),
    ]
