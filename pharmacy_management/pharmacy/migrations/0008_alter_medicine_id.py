# Generated by Django 4.2.19 on 2025-04-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_alter_medicine_category_alter_medicine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
