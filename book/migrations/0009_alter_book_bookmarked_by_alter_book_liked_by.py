# Generated by Django 4.2.5 on 2023-10-30 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0008_book_bookmarked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookmarked_by',
            field=models.ManyToManyField(related_name='bookmarked_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]