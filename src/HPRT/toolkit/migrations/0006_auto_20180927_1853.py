# Generated by Django 2.0.2 on 2018-09-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0005_auto_20180925_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalhealth',
            name='gh1',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Poor'), (2, '2 = Fair'), (3, '3 = Good'), (4, '4 = Very Good'), (5, '5 = Excellent')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh10',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = No'), (2, '2 = No, but trying to obtain work'), (3, '3 = Yes')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh11',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Yes'), (2, '2 = Yes and has been referred'), (3, '3 = No')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh12',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Yes'), (2, '2 = Yes and has been referred'), (3, '3 = No')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh2',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = None'), (2, '2 = A Little'), (3, '3 = Some'), (4, '4 = Quite A Lot'), (5, '5 = Very Much')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh3',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Extremely'), (2, '2 = Quite A Lot'), (3, '3 = Moderately'), (4, '4 = Slightly'), (5, '5 = Not At All')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh4',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Seven'), (2, '2 = Five to Seven'), (3, '3 = Three to Five'), (4, '4 = One to Three'), (5, '5 = Zero')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh5',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = None'), (2, '2 = Less than Four'), (3, '3 = Four to Five'), (4, '4 = Five to Seven'), (5, '5 = More than Seven')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh6',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Daily'), (2, '2 = Weekly'), (3, '3 = Monthly'), (4, '4 = Yearly'), (5, '5 = No')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh7',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Zero'), (2, '2 = One to Three'), (3, '3 = Three to Five'), (4, '4 = Five to Seven'), (5, '5 = More than Seven')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh8',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = Zero'), (2, '2 = One to Three'), (3, '3 = Three to Five'), (4, '4 = Five to Seven'), (5, '5 = More than Seven')], null=True),
        ),
        migrations.AlterField(
            model_name='generalhealth',
            name='gh9',
            field=models.IntegerField(choices=[('', 'Choose one'), (1, '1 = No'), (2, '2 = Yes')], null=True),
        ),
    ]