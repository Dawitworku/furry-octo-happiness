# Generated by Django 2.2 on 2020-09-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lec_app', '0004_geocache_dragons_that_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geocache',
            name='dragons_that_found',
            field=models.ManyToManyField(related_name='found_geocache', to='lec_app.Dragon'),
        ),
    ]
