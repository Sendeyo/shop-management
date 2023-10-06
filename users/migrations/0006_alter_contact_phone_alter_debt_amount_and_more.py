# Generated by Django 4.2.4 on 2023-10-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_debt_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='debt',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='debt',
            name='category',
            field=models.CharField(choices=[('owed', 'Owed'), ('owing', 'Owing')], max_length=20, null=True),
        ),
    ]
