# Generated by Django 4.1.3 on 2022-12-02 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BashFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='bash_file')),
                ('uploaded_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
