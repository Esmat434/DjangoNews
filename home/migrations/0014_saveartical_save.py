# Generated by Django 5.1.2 on 2024-12-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_answercomment_username_saveartical'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveartical',
            name='save',
            field=models.BooleanField(default=False),
        ),
    ]