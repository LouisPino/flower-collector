# Generated by Django 4.2.5 on 2023-09-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_watering_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aridity', models.CharField(max_length=1)),
                ('temperature', models.CharField(choices=[('C', 'Cold'), ('M', 'Medium'), ('H', 'Hot')], max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='flower',
            name='days_between_watering',
            field=models.IntegerField(verbose_name='Ideal # of days between watering'),
        ),
        migrations.AddField(
            model_name='flower',
            name='preferred_location',
            field=models.ManyToManyField(to='main_app.location'),
        ),
    ]