# Generated by Django 3.1.1 on 2020-09-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatros', '0003_auto_20200930_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]