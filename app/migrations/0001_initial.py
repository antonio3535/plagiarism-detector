# Generated by Django 3.0.4 on 2020-04-19 13:54

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, db_index=True, max_length=128)),
                ('metadata', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=191, null=True)),
                ('author', models.CharField(blank=True, max_length=191, null=True)),
                ('content', models.FileField(db_index=True, max_length=191, unique=True, upload_to=app.models._get_upload_path)),
                ('text', models.FileField(max_length=191, upload_to='text/')),
                ('html', models.FileField(max_length=191, upload_to='html/')),
                ('keyword', models.CharField(blank=True, max_length=191, null=True)),
                ('size_bytes', models.IntegerField(db_index=True, default=0)),
                ('fingerprint', models.FileField(max_length=191, upload_to='fingerprint/')),
                ('is_dataset', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('uploaded', 'Uploaded'), ('process', 'Process'), ('finished', 'Finished')], default='uploaded', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DB Insertion Time')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DB Modification Time')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(db_index=True, max_length=191, unique=True, upload_to=app.models._similarity_result_path)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DB Insertion Time')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DB Modification Time')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='similarity', to='app.Document')),
            ],
        ),
    ]
