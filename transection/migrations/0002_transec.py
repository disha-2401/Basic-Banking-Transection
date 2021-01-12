# Generated by Django 3.0.5 on 2021-01-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('senderName', models.IntegerField(max_length=30)),
                ('receiver', models.IntegerField(max_length=30)),
                ('amount', models.IntegerField(max_length=30)),
            ],
        ),
    ]