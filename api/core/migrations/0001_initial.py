# Generated by Django 5.0.1 on 2024-01-07 12:15

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
