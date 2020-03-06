# Generated by Django 3.0.3 on 2020-03-06 02:39

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsmap', '0008_auto_20200301_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapshot',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='municipality',
            name='centerpoint',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
