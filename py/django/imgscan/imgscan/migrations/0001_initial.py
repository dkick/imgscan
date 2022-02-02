# Generated by Django 4.0.2 on 2022-02-02 19:38

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import imgscan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgObject',
            fields=[
                ('label', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('imgfile', models.FileField(upload_to=imgscan.models.imgpath)),
                ('detect', models.BooleanField(default=True)),
                ('objects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imgscan.imgobject')),
            ],
            managers=[
                ('dbobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
