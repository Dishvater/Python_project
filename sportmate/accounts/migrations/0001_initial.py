# Generated by Django 3.0.8 on 2020-07-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=30)),
                ('password', models.TextField(max_length=30)),
                ('first_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=30)),
                ('date_of_birth', models.DateTimeField(blank=True, max_length=10, null=True)),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
