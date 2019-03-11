# Generated by Django 2.1.2 on 2019-01-06 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0003_auto_20190106_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=600)),
                ('discussion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussion.CreateDiscussion')),
                ('message_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussion.CreateDiscussion')),
                ('discussion_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]