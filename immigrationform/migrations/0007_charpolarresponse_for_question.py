# Generated by Django 2.1.3 on 2018-12-06 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('immigrationform', '0006_auto_20181206_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='charpolarresponse',
            name='for_question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='immigrationform.PolarQuestion'),
        ),
    ]
