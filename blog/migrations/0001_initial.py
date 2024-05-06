# Generated by Django 5.0.4 on 2024-05-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, max_length=5000, null=True)),
                ('inside_content', models.TextField(blank=True, max_length=10000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/')),
                ('author', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
            ],
        ),
    ]
