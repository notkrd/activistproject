# Generated by Django 2.1.3 on 2018-12-06 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immigrationform', '0005_auto_20181206_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='multi_choice_answers',
        ),
        migrations.RemoveField(
            model_name='character',
            name='polar_answers',
        ),
        migrations.RemoveField(
            model_name='charmultiresponse',
            name='for_question',
        ),
        migrations.RemoveField(
            model_name='charpolarresponse',
            name='for_question',
        ),
    ]
