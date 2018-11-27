# Generated by Django 2.1.3 on 2018-11-25 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_scores', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FreeResponse',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='immigrationform.Answer')),
                ('answer_val', models.CharField(max_length=120)),
            ],
            bases=('immigrationform.answer',),
        ),
        migrations.CreateModel(
            name='MultiChoiceResponse',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='immigrationform.Answer')),
                ('choice_val', models.TextField()),
            ],
            bases=('immigrationform.answer',),
        ),
        migrations.AddField(
            model_name='question',
            name='active_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='immigrationform.Answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='for_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immigrationform.Question'),
        ),
    ]
