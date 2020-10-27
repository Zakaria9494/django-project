# Generated by Django 2.2.3 on 2019-10-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBooks', '0007_auto_20191013_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buch',
            name='status',
            field=models.CharField(choices=[('nicht existiert', 'nicht existiert'), ('verfügbar', 'verfügbar'), ('nicht verfügbar', 'nicht verfügbar'), ('ausgeliehen', 'ausgeliehen')], default='', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('erstes Semester', 'erstes Semester'), ('sechstes Semester', 'sechstes Semester'), ('drittes Semester', 'drittes Semester'), ('fünftes Semester', 'fünftes Semester'), ('viertes Semester', 'viertes Semester'), ('zweites Semester', 'zweites Semester')], default='', max_length=50, null=True, unique=True),
        ),
    ]
