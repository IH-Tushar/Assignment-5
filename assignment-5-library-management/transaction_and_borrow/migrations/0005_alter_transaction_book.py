# Generated by Django 4.2.7 on 2024-03-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_rename_price_book_borrowing_price_and_more'),
        ('transaction_and_borrow', '0004_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='first_app.book'),
        ),
    ]