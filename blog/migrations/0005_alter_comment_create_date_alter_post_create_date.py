# Generated by Django 4.0.4 on 2022-06-08 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_create_date_alter_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 12, 34, 44, 593080, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 12, 34, 44, 592655, tzinfo=utc)),
        ),
    ]
