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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('education_level', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=150)),
                ('interests', models.TextField(help_text='Comma separated interests')),
                ('work_preference', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('work_from_home', 'Work From Home'), ('freelancing', 'Freelancing')], max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skills', models.ManyToManyField(blank=True, to='users.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
