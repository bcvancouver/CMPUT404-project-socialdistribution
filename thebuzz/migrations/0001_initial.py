# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=2000)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myImg', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'No Title', max_length=100)),
                ('source', models.CharField(max_length=2000)),
                ('origin', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('contentType', models.CharField(default=b'text/plain', max_length=2000)),
                ('published', models.DateTimeField(auto_now=True)),
                ('visibility', models.CharField(default=b'PUBLIC', max_length=20)),
                ('visibleTo', models.CharField(max_length=1000, blank=True)),
                ('associated_author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('displayName', models.CharField(max_length=200, blank=True)),
                ('github', models.CharField(max_length=200, blank=True)),
                ('firstName', models.CharField(max_length=200, blank=True)),
                ('lastName', models.CharField(max_length=200, blank=True)),
                ('email', models.CharField(max_length=400, blank=True)),
                ('bio', models.CharField(max_length=2000, blank=True)),
                ('followers', models.ManyToManyField(related_name='my_followers', to='thebuzz.Profile', blank=True)),
                ('following', models.ManyToManyField(related_name='who_im_following', to='thebuzz.Profile', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='thebuzz.Profile', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='img',
            name='associated_post',
            field=models.ForeignKey(to='thebuzz.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='associated_post',
            field=models.ForeignKey(to='thebuzz.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='thebuzz.Profile'),
        ),
    ]
