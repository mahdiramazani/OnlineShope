# Generated by Django 4.1 on 2022-08-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='titel',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]