# Generated by Django 2.1 on 2018-08-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hajjer',
            fields=[
                ('RFID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
                ('Balance', models.FloatField(default=0.0)),
            ],
        ),
    ]