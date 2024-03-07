# Generated by Django 5.0.2 on 2024-03-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_signeduser_id_alter_signeduser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='user_message',
            field=models.TextField(default='Asia/Kolkata'),
            preserve_default=False,
        ),
    ]