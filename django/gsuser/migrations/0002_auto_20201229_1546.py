# Generated by Django 3.1.4 on 2020-12-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
