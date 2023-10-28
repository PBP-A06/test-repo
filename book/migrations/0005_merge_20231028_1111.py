# Generated by Django 4.2.4 on 2023-10-28 04:11

from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")

class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_bookdescription_book_book_description_and_more'),
        ('book', '0004_auto_20231028_1109'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]