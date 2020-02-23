# Generated by Django 2.2.3 on 2020-01-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0002_auto_20191231_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='status',
        ),
        migrations.AddField(
            model_name='notes',
            name='relshortlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relshortlist', to='functionality.shortlist'),
        ),
        migrations.AddField(
            model_name='shortlist',
            name='note',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
