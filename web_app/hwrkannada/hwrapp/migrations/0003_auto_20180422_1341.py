# Generated by Django 2.0.4 on 2018-04-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwrapp', '0002_auto_20180421_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentimage',
            name='id',
        ),
        migrations.AddField(
            model_name='documentimage',
            name='image_id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]