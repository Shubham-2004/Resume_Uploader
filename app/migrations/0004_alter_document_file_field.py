# Generated by Django 4.2.11 on 2024-04-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_document_delete_dog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file_field",
            field=models.FileField(blank=True, upload_to="doc"),
        ),
    ]