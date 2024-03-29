# Generated by Django 4.1.5 on 2023-03-18 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_cours_cost_group_alter_cours_cost_individual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('pupil', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.pupil')),
            ],
            options={
                'verbose_name': 'Календарь',
            },
        ),
    ]
