# Generated by Django 4.1.2 on 2022-10-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HighestMonthlyGrossIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
                ('highest_gross_income', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
