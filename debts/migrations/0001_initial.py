# Generated by Django 3.0.5 on 2020-04-29 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_confirm', models.BooleanField()),
                ('resiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.UserProfile')),
            ],
        ),
    ]
