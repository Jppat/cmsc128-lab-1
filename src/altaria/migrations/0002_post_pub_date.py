# Generated by Django 3.2.4 on 2021-06-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
