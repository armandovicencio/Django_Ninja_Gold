# Generated by Django 4.0.2 on 2022-02-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='temperatura',
            field=models.IntegerField(null=True),
        ),
    ]
