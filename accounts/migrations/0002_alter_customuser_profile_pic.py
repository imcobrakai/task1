# Generated by Django 3.2.15 on 2022-08-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Profile Picture'),
        ),
    ]