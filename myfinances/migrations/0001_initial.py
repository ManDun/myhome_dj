# Generated by Django 3.0.5 on 2020-05-04 08:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('food', 'Food'), ('entertainment', 'Entertainment'), ('living', 'Living')], default='food', max_length=20)),
                ('amount', models.FloatField(max_length=10)),
                ('details', models.TextField(max_length=256, null=True)),
                ('date_of_expense', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=50, null=True)),
                ('date_of_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('contents', models.BinaryField(null=True)),
                ('size', models.FloatField(default=0)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfinances.Expenses')),
            ],
        ),
    ]