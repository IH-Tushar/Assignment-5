# Generated by Django 4.2.7 on 2024-03-04 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0003_rename_price_book_borrowing_price_and_more'),
        ('transaction_and_borrow', '0002_transaction_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='first_app.book')),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowinghistory',
            name='return_date',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
