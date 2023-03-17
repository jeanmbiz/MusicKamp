# Generated by Django 4.0.7 on 2023-03-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This field must be unique.'}, max_length=254, unique=True),
        ),
    ]
