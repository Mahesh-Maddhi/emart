# Generated by Django 5.0.1 on 2024-04-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_product_brand_cart_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('discountPercentage', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=255)),
                ('images', models.JSONField()),
            ],
        ),
    ]
