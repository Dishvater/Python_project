# Generated by Django 2.2.13 on 2020-07-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smate', '0006_event_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to='smate.User'),
        ),
    ]