# Generated by Django 2.0.4 on 2018-04-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit',
            name='ex_id',
            field=models.CharField(default='', help_text='Enter the exhibit ID number. Must be unique!', max_length=2),
        ),
        migrations.RemoveField(
            model_name='exhibit',
            name='neighbors',
        ),
        migrations.AddField(
            model_name='exhibit',
            name='neighbors',
            field=models.CharField(default='', help_text="Enter ID's of neighbor exhibits, \n\tseparated by commas.\n\tI.E. 1,2,3", max_length=2),
        ),
    ]
