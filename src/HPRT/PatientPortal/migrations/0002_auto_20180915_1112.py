# Generated by Django 2.0.6 on 2018-09-15 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PatientPortal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='docpat',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='docpat',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Patient'),
        ),
        migrations.AlterUniqueTogether(
            name='docpat',
            unique_together={('doctor', 'patient')},
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('patient', 'appt_time')},
        ),
    ]