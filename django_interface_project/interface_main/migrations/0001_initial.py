# Generated by Django 2.2.1 on 2019-09-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='服务的名称')),
                ('description', models.CharField(default='', max_length=2000, verbose_name='服务的描述')),
                ('parent', models.IntegerField(default=0, verbose_name='服务的父节点')),
            ],
        ),
    ]