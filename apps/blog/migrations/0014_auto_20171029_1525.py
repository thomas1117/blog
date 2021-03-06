# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 15:25
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20171029_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('javascript', 'Javascript'), ('python', 'Python'), ('html', 'HTML'), ('css', 'CSS'), ('c', 'C')])), ('code', wagtail.wagtailcore.blocks.RawHTMLBlock())), icon='code')), ('raw_code', wagtail.wagtailcore.blocks.StructBlock((('code', wagtail.wagtailcore.blocks.RawHTMLBlock()),), icon='placeholder')), ('image', wagtail.wagtailcore.blocks.StructBlock((('caption', wagtail.wagtailcore.blocks.RichTextBlock(max_length=255)),), icon='image')))),
        ),
    ]
