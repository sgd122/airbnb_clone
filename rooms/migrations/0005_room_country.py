# Generated by Django 2.2.5 on 2019-12-30 12:10

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20191229_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
