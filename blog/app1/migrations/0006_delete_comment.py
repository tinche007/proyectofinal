# Generated by Django 4.2.4 on 2023-08-15 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_provincia_opinion_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
