# Generated by Django 2.2.4 on 2019-08-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190817_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='bio',
            field=models.CharField(default='Insert Bio Here...', help_text='Some words about yourself...', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(help_text='Write your comment', max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(help_text='Begin writing...', max_length=3000),
        ),
    ]