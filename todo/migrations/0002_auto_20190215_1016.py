# Generated by Django 2.1.7 on 2019-02-15 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]