# Generated by Django 4.2.5 on 2023-10-29 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_book_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]