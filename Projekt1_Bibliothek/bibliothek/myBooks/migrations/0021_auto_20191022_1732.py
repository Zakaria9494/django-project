# Generated by Django 2.2.3 on 2019-10-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBooks', '0020_auto_20191019_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buch',
            name='status',
            field=models.CharField(choices=[('nicht existiert', 'nicht existiert'), ('ausgeliehen', 'ausgeliehen'), ('nicht verfügbar', 'nicht verfügbar'), ('verfügbar', 'verfügbar')], default='', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('drittes Semester', 'drittes Semester'), ('fünftes Semester', 'fünftes Semester'), ('sechstes Semester', 'sechstes Semester'), ('viertes Semester', 'viertes Semester'), ('erstes Semester', 'erstes Semester'), ('zweites Semester', 'zweites Semester')], default='', max_length=50, null=True, unique=True),
        ),
    ]
