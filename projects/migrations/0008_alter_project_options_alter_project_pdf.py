# Generated by Django 4.0.2 on 2022-03-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_pdf_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='project',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='static/media'),
        ),
    ]
