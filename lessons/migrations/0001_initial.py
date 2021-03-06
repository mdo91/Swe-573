# Generated by Django 2.0.2 on 2019-05-13 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20190428_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=255)),
                ('lesson_hierarchy', models.IntegerField()),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
    ]
