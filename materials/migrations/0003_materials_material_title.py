# Generated by Django 2.0.2 on 2019-05-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_materials_topic_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='material_title',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
