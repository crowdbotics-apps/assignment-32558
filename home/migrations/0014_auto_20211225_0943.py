# Generated by Django 2.2.24 on 2021-12-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211225_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='screen_shot',
            field=models.URLField(blank=True, default='', editable=False, verbose_name='Screenshot'),
        ),
    ]
