# Generated by Django 4.1.4 on 2023-01-10 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userprofile_companay_userprofile_designation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='companay',
            new_name='company',
        ),
    ]
