# Generated by Django 3.1.7 on 2021-03-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0004_blogindexpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
    ]
