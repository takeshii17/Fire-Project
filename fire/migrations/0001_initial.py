# Generated by Django 4.2.11 on 2024-12-07 09:23

from django.db import migrations, models
import django.db.models.deletion
import fire.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FireStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Fire Station',
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_time', models.DateTimeField(blank=True, null=True, validators=[fire.models.validate_not_future])),
                ('severity_level', models.CharField(choices=[('Minor Fire', 'Minor Fire'), ('Moderate Fire', 'Moderate Fire'), ('Major Fire', 'Major Fire')], max_length=45)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Incident',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='WeatherConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=10, validators=[fire.models.validate_non_negative])),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=10, validators=[fire.models.validate_non_negative])),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=10, validators=[fire.models.validate_non_negative])),
                ('weather_description', models.CharField(max_length=150)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fire.incident')),
            ],
            options={
                'verbose_name': 'Weather Condition',
            },
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fire.locations'),
        ),
        migrations.CreateModel(
            name='FireTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('truck_number', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('capacity', models.CharField(max_length=150)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fire.firestation')),
            ],
            options={
                'verbose_name': 'Fire Truck',
            },
        ),
        migrations.CreateModel(
            name='Firefighters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('rank', models.CharField(max_length=150)),
                ('experience_level', models.CharField(choices=[('Probationary Firefighter', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=150)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fire.firestation')),
            ],
            options={
                'verbose_name': 'Firefighter',
            },
        ),
    ]
