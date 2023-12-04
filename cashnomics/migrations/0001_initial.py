# Generated by Django 4.2.6 on 2023-11-12 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('industry', models.CharField(choices=[('Agriculture', 'Agriculture'), ('Apparel', 'Apparel'), ('Automotive', 'Automotive'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'), ('Chemicals', 'Chemicals'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Consumer Goods', 'Consumer Goods'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'), ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Environmental', 'Environmental'), ('Finance', 'Finance'), ('Food and Beverage', 'Food and Beverage'), ('Government', 'Government'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Insurance', 'Insurance'), ('Machinery', 'Machinery'), ('Manufacturing', 'Manufacturing'), ('Media', 'Media'), ('Non-profit', 'Non-profit'), ('Pharmaceuticals', 'Pharmaceuticals'), ('Real Estate', 'Real Estate'), ('Retail', 'Retail'), ('Sports', 'Sports'), ('Technology', 'Technology'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities'), ('Other', 'Other')], max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsInvestments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('savings_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('savings_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('etf_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('etf_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('money_after_y1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('money_after_y5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('income_after_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpensesForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('cost_sh_bills', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_travel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_groceries', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_ent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_other', models.DecimalField(decimal_places=2, max_digits=10)),
                ('money_aftercosts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_type', models.CharField(max_length=255)),
                ('img_ref', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]