# Generated by Django 3.0.5 on 2020-04-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
