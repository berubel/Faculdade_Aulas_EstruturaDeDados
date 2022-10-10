# Generated by Django 4.1.1 on 2022-10-10 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_users_receipt_wallet_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='transfer_user',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='wallet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='api.wallet'),
        ),
        migrations.AlterField(
            model_name='users',
            name='enrollment',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.URLField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
