# Generated by Django 4.0.8 on 2022-12-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_modelx_created_at_modelx_update_at_modely'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelx',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='modelx',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='modely',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='modely',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
