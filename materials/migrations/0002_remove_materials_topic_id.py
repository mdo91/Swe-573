# Generated by Django 2.0.2 on 2019-05-18 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='topic_id',
        ),
    ]