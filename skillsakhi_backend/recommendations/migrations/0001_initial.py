from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
                ('education_required', models.CharField(max_length=120)),
                ('demand_level', models.CharField(max_length=40)),
                ('preferred_work_type', models.CharField(max_length=20)),
                ('interests', models.TextField(help_text='Comma separated interest tags')),
            ],
        ),
        migrations.CreateModel(
            name='CareerSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_skills', to='recommendations.career')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.skill')),
            ],
            options={'unique_together': {('career', 'skill')}},
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('provider', models.CharField(max_length=80)),
                ('link', models.URLField()),
                ('estimated_duration', models.CharField(max_length=60)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='recommendations.career')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('company', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('source', models.CharField(max_length=80)),
                ('link', models.URLField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='recommendations.career')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suitability_score', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendations.career')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
