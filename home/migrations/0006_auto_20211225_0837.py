# Generated by Django 2.2.24 on 2021-12-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211225_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='domain_name',
            field=models.URLField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='framework',
            field=models.TextField(choices=[('django', 'Django'), ('react_native', 'React Native')]),
        ),
        migrations.AlterField(
            model_name='app',
            name='screen_shot',
            field=models.URLField(default='', verbose_name='Screenshot'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='type',
            field=models.TextField(choices=[('web', 'Web'), ('mobile', 'Mobile')]),
        ),
    ]