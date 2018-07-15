# Generated by Django 2.0.4 on 2018-05-02 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20180501_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='category',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurants', to='feed.Category'),
        ),
    ]
