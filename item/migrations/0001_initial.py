# Generated by Django 4.1.13 on 2024-04-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sellerID', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('stock', models.BooleanField()),
                ('image', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Comprado', 'Comprado'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')], default='Comprado', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('review', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('image', models.URLField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('total', models.FloatField()),
                ('cart', models.JSONField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
