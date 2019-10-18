# Generated by Django 2.2.1 on 2019-09-24 10:13

from django.db import migrations, models
import django.db.models.deletion
import interface_main.models.fields.json_field


class Migration(migrations.Migration):

    dependencies = [
        ('interface_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='接口的名称')),
                ('description', models.CharField(default='', max_length=2000, verbose_name='描述')),
                ('path', models.CharField(default='', max_length=500, verbose_name='path')),
                ('method', models.CharField(default='get', max_length=20, verbose_name='方法')),
                ('params_type', models.CharField(default='json', max_length=20, verbose_name='json还是form')),
                ('asserts', interface_main.models.fields.json_field.JsonField(verbose_name='断言')),
                ('headers', interface_main.models.fields.json_field.JsonField(verbose_name='头部')),
                ('params', interface_main.models.fields.json_field.JsonField(verbose_name='参数')),
                ('response', models.TextField(default='', verbose_name='响应')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_main.Service')),
            ],
        ),
    ]
