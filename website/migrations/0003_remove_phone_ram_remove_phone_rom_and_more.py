# Generated by Django 4.2.4 on 2023-08-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_phone_screensize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='rom',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='screenSize',
        ),
        migrations.AddField(
            model_name='phone',
            name='cameras',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='phone',
            name='memory',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='processor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='screen',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
