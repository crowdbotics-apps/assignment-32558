# Generated by Django 2.2.24 on 2021-12-25 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211225_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='app',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_app', to='home.App'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_plan', to='home.Plan'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
