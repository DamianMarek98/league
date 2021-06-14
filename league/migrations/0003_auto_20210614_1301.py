# Generated by Django 3.2.3 on 2021-06-14 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('league', '0002_auto_20210614_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_created'], 'verbose_name': 'Komentarz', 'verbose_name_plural': 'Komentarze'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Mecz', 'verbose_name_plural': 'Mecze'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Zawodnik', 'verbose_name_plural': 'Zawodnicy'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Zespol', 'verbose_name_plural': 'Zespoly'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.match', verbose_name='Mecz'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Tekst'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Uzytkownik'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_score',
            field=models.IntegerField(null=True, verbose_name='Bramki_gosc'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_team', to='league.team', verbose_name='Gosc'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.IntegerField(null=True, verbose_name='Bramki_gosp'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_team', to='league.team', verbose_name='Gospodarz'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Numer'),
        ),
        migrations.AlterField(
            model_name='player',
            name='surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.team', verbose_name='Zespol'),
        ),

        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.IntegerField(null=True, verbose_name='Punkty'),
        ),
    ]