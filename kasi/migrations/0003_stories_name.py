# Generated by Django 2.1.7 on 2019-03-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasi', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='name',
            field=models.CharField(default='the triumphalist', max_length=20),
            preserve_default=False,
        ),
    ]
