# Generated by Django 3.0.5 on 2020-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
            ],
        ),
    ]
