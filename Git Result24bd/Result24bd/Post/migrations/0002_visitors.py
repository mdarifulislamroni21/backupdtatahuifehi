# Generated by Django 3.2.7 on 2021-09-13 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_blog', to='Post.post')),
            ],
        ),
    ]
