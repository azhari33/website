# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 08:28
from __future__ import unicode_literals

import django.db.models.deletion
import markdownx.models
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=200, verbose_name='Category Name')),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', markdownx.models.MarkdownxField(verbose_name='Markdown')),
                ('is_created', models.DateTimeField(default=timezone.now)),
                ('comment_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='app_author.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_title', models.CharField(max_length=225, verbose_name='Title')),
                ('forum_content', markdownx.models.MarkdownxField(verbose_name='Content (Use Markdown)')),
                ('is_created', models.DateTimeField(blank=True, default=timezone.now, null=True)),
                ('is_modified', models.DateTimeField(blank=True, default=timezone.now, null=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('forum_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_forums', to='app_author.Profile')),
                ('forum_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_forum.Category', verbose_name='Category')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_comments', to='app_forum.Forum'),
        ),
    ]
