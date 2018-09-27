# Generated by Django 2.0.2 on 2018-09-26 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0004_generalhealth'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalhealth',
            name='gh10',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh11',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh12',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh2',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh3',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh4',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh5',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh6',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh7',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh8',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
        migrations.AddField(
            model_name='generalhealth',
            name='gh9',
            field=models.IntegerField(choices=[(1, 1), (2, 2)], default=None),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh1',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
    ]