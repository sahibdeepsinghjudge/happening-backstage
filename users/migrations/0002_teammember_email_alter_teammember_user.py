# Generated by Django 4.2 on 2024-09-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teammember",
            name="email",
            field=models.EmailField(default="abc@gmail.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="user",
            field=models.CharField(max_length=100),
        ),
    ]
