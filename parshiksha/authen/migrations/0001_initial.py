# Generated by Django 3.0.5 on 2020-04-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('passoword', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('imageLink', models.CharField(max_length=1000)),
                ('verified', models.BooleanField()),
            ],
        ),
    ]
