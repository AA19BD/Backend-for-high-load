# Generated by Django 3.2.16 on 2022-11-20 17:34

from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0003_courier_staff'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_photos', validators=[utils.validators.validate_extension, utils.validators.validate_size])),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='ingredients')),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'food',
            },
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Wear',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('size', models.CharField(blank=True, max_length=10, verbose_name='size')),
                ('materials', models.TextField(blank=True, null=True, verbose_name='materials')),
            ],
            options={
                'verbose_name': 'wear',
                'verbose_name_plural': 'wear',
            },
            bases=('main.product',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delivered', models.BooleanField(default=False)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_.client')),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_.courier')),
                ('products', models.ManyToManyField(blank=True, to='main.Product')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
    ]
