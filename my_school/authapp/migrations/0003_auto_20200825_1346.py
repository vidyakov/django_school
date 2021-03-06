# Generated by Django 3.0.8 on 2020-08-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200825_1346'),
        ('authapp', '0002_auto_20200825_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='sex',
            field=models.CharField(choices=[('m', 'Man'), ('f', 'Woman')], max_length=1),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mainapp.Tag'),
        ),
    ]
