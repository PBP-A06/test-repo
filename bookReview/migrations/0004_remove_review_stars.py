# Generated by Django 4.2.5 on 2023-10-30 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookReview', '0003_remove_review_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
    ]