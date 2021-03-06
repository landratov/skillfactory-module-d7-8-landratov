# Generated by Django 3.0.8 on 2020-07-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20200712_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='friend_book', to='p_library.Book', verbose_name='Книги'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.TextField(verbose_name='Имя'),
        ),
    ]
