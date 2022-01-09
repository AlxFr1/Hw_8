# Generated by Django 4.0 on 2022-01-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_8_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField()),
                ('method', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]