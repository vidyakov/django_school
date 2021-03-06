# Generated by Django 3.0.8 on 2020-09-10 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200825_1354'),
        ('courseapp', '0003_auto_20200825_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactivelesson',
            name='lesson_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inter_lesson', to='courseapp.LessonInfo'),
        ),
        migrations.AlterField(
            model_name='lessoninfo',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='mainapp.Course'),
        ),
        migrations.AlterField(
            model_name='lessoninfo',
            name='materials',
            field=models.ManyToManyField(blank=True, to='courseapp.AdditionalMaterial'),
        ),
    ]
