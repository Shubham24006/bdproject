# Generated by Django 2.0.7 on 2018-07-26 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BDapp', '0002_auto_20180726_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='project',
        ),
    ]