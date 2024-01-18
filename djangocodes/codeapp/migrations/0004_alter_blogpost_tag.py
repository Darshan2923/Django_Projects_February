# Generated by Django 4.2.7 on 2024-01-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0003_alter_blogpost_options_remove_profile_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tag',
            field=models.CharField(choices=[('1', 'general'), ('2', 'python'), ('3', 'django'), ('4', 'web designing')], default='General', max_length=20),
        ),
    ]