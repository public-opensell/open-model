# Generated by Django 2.2.5 on 2019-09-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100)),
                ('bauther', models.CharField(max_length=100)),
                ('bprices', models.FloatField(default=0)),
            ],
        ),
    ]
