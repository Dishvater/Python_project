# Generated by Django 2.2.13 on 2020-08-07 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smate', '0002_auto_20200807_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='smate.City'),
            preserve_default=False,
        ),
    ]
