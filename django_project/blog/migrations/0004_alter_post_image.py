# Generated by Django 4.1 on 2022-09-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='tech_blog_01.jpg', null=True, upload_to='post_image'),
        ),
    ]
