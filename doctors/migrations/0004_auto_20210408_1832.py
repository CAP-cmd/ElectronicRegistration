# Generated by Django 3.1.7 on 2021-04-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20210406_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refreshercourse',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refresher_courses', to='doctors.doctor'),
        ),
        migrations.AlterField(
            model_name='refreshercourse',
            name='name_courses',
            field=models.TextField(verbose_name='Название курса'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='name_work',
            field=models.TextField(verbose_name='Работа'),
        ),
    ]
