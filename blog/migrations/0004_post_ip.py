# Generated by Django 4.1.5 on 2023-02-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(editable=False, null=True),
        ),
    ]