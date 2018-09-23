# Generated by Django 2.1 on 2018-09-23 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名称', models.CharField(max_length=50, unique=True)),
                ('描述', models.TextField(blank=True)),
                ('图片', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Category',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名称', models.CharField(max_length=100, unique=True)),
                ('描述', models.TextField(blank=True)),
                ('图片', models.ImageField(blank=True, upload_to='category')),
                ('价格', models.DecimalField(decimal_places=2, max_digits=10)),
                ('上架情况', models.BooleanField(default=True)),
                ('创建时间', models.DateField(auto_now_add=True)),
                ('修改时间', models.DateField(auto_now_add=True)),
                ('库存', models.IntegerField(default=0)),
                ('所属类别', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Category')),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'Product',
                'ordering': ('-创建时间',),
            },
        ),
    ]
