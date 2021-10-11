# Generated by Django 3.2.8 on 2021-10-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2021-10-05')),
                ('due_date', models.DateField(default='2021-10-05')),
                ('user', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]