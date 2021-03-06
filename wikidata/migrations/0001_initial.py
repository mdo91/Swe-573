# Generated by Django 2.0.2 on 2019-05-12 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20190428_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wikidata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wikiTitle', models.CharField(max_length=255)),
                ('wikiLink', models.TextField()),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
    ]
