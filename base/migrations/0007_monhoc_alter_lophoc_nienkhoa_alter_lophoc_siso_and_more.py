# Generated by Django 4.1.3 on 2023-01-05 15:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_subject_remove_hocsinh_lophoc_grade_hocsinh_lophoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='MONHOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TENMONHOC', models.CharField(max_length=200)),
                ('DIEMCHUAN', models.FloatField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='NIENKHOA',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(3000)]),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='SISO',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.monhoc'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
