# Generated by Django 5.1.2 on 2024-10-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stf', '0011_profile_solved_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='solved_tasks',
            field=models.CharField(max_length=10000000, null=True),
        ),
    ]
