# Generated by Django 4.0.2 on 2022-03-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=15)),
                ('email_id', models.CharField(max_length=30)),
            ],
        ),
    ]
