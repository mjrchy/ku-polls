# Generated by Django 4.1.1 on 2023-09-09 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 9, 17, 32, 27, 983314, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
