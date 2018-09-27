# Generated by Django 2.0.2 on 2018-09-25 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PatientPortal', '0004_auto_20180923_1301'),
        ('toolkit', '0003_auto_20180920_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gh1', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=None)),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Patient')),
            ],
        ),
    ]