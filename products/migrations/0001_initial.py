# Generated by Django 5.1.6 on 2025-02-28 12:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_img', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMetaInfo',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.CharField(blank=True, max_length=20, null=True)),
                ('product_unit', models.CharField(choices=[('kg', 'kg'), ('ml', 'ml'), ('L', 'L'), ('pcs', 'pcs')], max_length=100)),
                ('restrict', models.IntegerField()),
                ('is_restrict', models.BinaryField(default=False)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
