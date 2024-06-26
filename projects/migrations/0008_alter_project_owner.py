# Generated by Django 5.0.3 on 2024-04-02 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_options'),
        ('users', '0007_alter_message_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
