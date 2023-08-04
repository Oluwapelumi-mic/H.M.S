# Generated by Django 4.2.2 on 2023-08-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_mngt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Patient',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Speciality',
            new_name='speciality',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Mobile_No',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Mobile_No',
        ),
        migrations.AddField(
            model_name='doctor',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='patient',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
