# Generated by Django 3.2.21 on 2024-06-01 17:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='overview',
            field=models.TextField(default=datetime.datetime(2024, 6, 1, 17, 9, 27, 778482, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 6, 1, 17, 9, 31, 462680, tzinfo=utc), max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default=datetime.datetime(2024, 6, 1, 17, 10, 18, 478046, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
        ),
    ]