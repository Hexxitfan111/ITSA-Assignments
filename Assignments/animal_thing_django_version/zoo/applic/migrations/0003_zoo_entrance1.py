# Generated by Django 2.0.4 on 2018-05-05 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applic', '0002_remove_zoo_entrance1'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='entrance1',
            field=models.ForeignKey(default='', help_text='Select the zoo entrance:', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entrance', to='applic.Exhibit'),
        ),
    ]
