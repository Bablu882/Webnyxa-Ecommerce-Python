# Generated by Django 3.2.12 on 2022-02-04 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220203_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slugfiy'),
        ),
    ]
