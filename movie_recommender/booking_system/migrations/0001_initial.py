# Generated by Django 2.0.3 on 2018-04-01 14:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.FloatField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('popularity', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CastType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CrewProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('link', models.TextField(default='')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('location_lat', models.FloatField(default=0)),
                ('location_long', models.FloatField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.City')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('synopsis', models.TextField(default='')),
                ('release_date', models.DateField()),
                ('tagline', models.TextField(default='')),
                ('imdb_id', models.CharField(max_length=20, unique=True)),
                ('crew', models.ManyToManyField(to='booking_system.Crew')),
                ('genres', models.ManyToManyField(to='booking_system.Genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Language')),
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
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.CharField(max_length=3)),
                ('col_id', models.CharField(max_length=5)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Screen')),
            ],
        ),
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Screen')),
            ],
        ),
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Location')),
            ],
        ),
        migrations.CreateModel(
            name='TheaterOwner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(default='', max_length=10)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Gender')),
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(default='', max_length=10)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Gender')),
                ('genre_pref', models.ManyToManyField(to='booking_system.Genre')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='booking_system.Booking')),
                ('ticket_price', models.FloatField(default=0)),
                ('taxes', models.FloatField(default=0)),
                ('service_charge', models.FloatField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('status', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking_system.StatusType')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.SeatType'),
        ),
        migrations.AddField(
            model_name='screen',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Theater'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.UserProfile'),
        ),
        migrations.AddField(
            model_name='crewprofile',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Gender'),
        ),
        migrations.AddField(
            model_name='crew',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.CrewProfile'),
        ),
        migrations.AddField(
            model_name='crew',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.CastType'),
        ),
        migrations.AddField(
            model_name='booking',
            name='seats',
            field=models.ManyToManyField(to='booking_system.Seat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Show'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_system.UserProfile'),
        ),
        migrations.AddField(
            model_name='aggregaterating',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking_system.Movie'),
        ),
        migrations.AlterUniqueTogether(
            name='show',
            unique_together={('movie', 'screen', 'show_time')},
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('row_id', 'col_id', 'screen')},
        ),
        migrations.AlterUniqueTogether(
            name='screen',
            unique_together={('theater', 'identifier')},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'movie')},
        ),
        migrations.AlterUniqueTogether(
            name='crew',
            unique_together={('profile', 'role')},
        ),
    ]
