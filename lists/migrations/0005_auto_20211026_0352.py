# Generated by Django 3.2.7 on 2021-10-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
