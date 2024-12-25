# Generated by Django 5.1.2 on 2024-11-28 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_comment_count_remove_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='avatar',
            field=models.ImageField(upload_to='static/images/main'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='static/images/information')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('artical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.artical')),
            ],
        ),
    ]