# Generated by Django 4.1.1 on 2022-12-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_customerontour_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="last_modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]