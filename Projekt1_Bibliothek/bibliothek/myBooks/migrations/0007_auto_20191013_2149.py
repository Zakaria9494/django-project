# Generated by Django 2.2.3 on 2019-10-13 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myBooks', '0006_auto_20191013_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=200)),
                ('nachname', models.CharField(max_length=200)),
                ('wohnort', models.CharField(max_length=200)),
                ('geburtsdatum', models.DateField(blank=True, default=None, null=True)),
                ('datum', models.DateField(blank=True, default=None, null=True)),
                ('semester', models.CharField(choices=[('sechstes Semester', 'sechstes Semester'), ('fünftes Semester', 'fünftes Semester'), ('erstes Semester', 'erstes Semester'), ('viertes Semester', 'viertes Semester'), ('drittes Semester', 'drittes Semester'), ('zweites Semester', 'zweites Semester')], default='', max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='buch',
            name='status',
            field=models.CharField(choices=[('nicht existiert', 'nicht existiert'), ('nicht verfügbar', 'nicht verfügbar'), ('ausgeliehen', 'ausgeliehen'), ('verfügbar', 'verfügbar')], default='', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='myBooks.Buch'),
        ),
    ]