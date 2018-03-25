# Generated by Django 2.0.2 on 2018-03-25 11:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('booking_system', '0004_auto_20180305_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_identifier', models.CharField(default='', max_length=100)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Show')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.SeatType')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_price', models.FloatField(default=0)),
                ('taxes', models.FloatField(default=0)),
                ('service_charge', models.FloatField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other')])),
                ('phone', models.CharField(default='', max_length=10)),
                ('genre_pref', models.ManyToManyField(to='booking_system.Genre')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.UserProfile'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.UserProfile'),
        ),
    ]
