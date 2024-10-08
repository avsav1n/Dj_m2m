# Generated by Django 5.1.1 on 2024-10-06 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag_scope_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематики статьи', 'verbose_name_plural': 'Тематики статей'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='articles', to='articles.tag', verbose_name='Разделы'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Название статьи'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Название раздела'),
        ),
    ]
