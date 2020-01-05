# Generated by Django 2.2.5 on 2020-01-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20191231_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='amenties',
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, help_text='편의시설', related_name='rooms', to='rooms.Amenity'),
        ),
    ]