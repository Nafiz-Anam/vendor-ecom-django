# Generated by Django 4.0.3 on 2022-03-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0018_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salerdetail',
            name='state',
        ),
        migrations.AlterField(
            model_name='salerdetail',
            name='gst_Number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='salerdetail',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
