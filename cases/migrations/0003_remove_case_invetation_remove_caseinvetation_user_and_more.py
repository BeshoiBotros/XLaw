# Generated by Django 5.0 on 2024-06-04 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_caseinvetation_org_approvment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='invetation',
        ),
        migrations.RemoveField(
            model_name='caseinvetation',
            name='user',
        ),
        migrations.AddField(
            model_name='case',
            name='case_status',
            field=models.CharField(choices=[('pending', 'قيد الانتظار'), ('reserved', 'محجوز')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='caseinvetation',
            name='the_case',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cases.case'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='caseinvetation',
            name='invetation_status',
            field=models.CharField(choices=[('pending', 'قيد الانتظار'), ('accepted', 'مقبول'), ('rejected', 'مرفوض')], default='pending', max_length=15),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.category')),
            ],
        ),
    ]
