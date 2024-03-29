# Generated by Django 5.0 on 2023-12-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_student_sno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='student',
            name='language',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='sno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
