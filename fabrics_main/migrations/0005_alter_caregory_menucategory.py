# Generated by Django 4.1.3 on 2022-12-12 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics_main', '0004_alter_caregory_menucategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregory',
            name='menucategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fabrics_main.menucategory'),
        ),
    ]
