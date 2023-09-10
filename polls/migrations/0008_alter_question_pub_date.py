# Generated by Django 4.1.1 on 2023-09-09 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
