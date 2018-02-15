# Generated by Django 2.0 on 2018-02-15 01:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('PatientPortal', '0002_auto_20180206_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAppointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('systolic_blood_pressure', models.IntegerField(null=True)),
                ('diastolic_blood_pressure', models.IntegerField(null=True)),
                ('tempurature', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('doctor_notes', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Drug_Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
                ('concentration', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('DOB', models.DateField(null=True)),
                ('blood_type', models.CharField(max_length=10, null=True)),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('allergies', models.TextField(default='')),
                ('current_medications', models.TextField(default='')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lack_of_shelter', models.BooleanField()),
                ('lack_of_food_or_water', models.BooleanField()),
                ('ill_health_without_access_to_medical_care', models.BooleanField()),
                ('confiscation_or_destruction_of_personal_property', models.BooleanField()),
                ('combat_situation', models.BooleanField()),
                ('forced_evacuation_under_dangerous_conditions', models.BooleanField()),
                ('beating_to_the_body', models.BooleanField()),
                ('rape', models.BooleanField()),
                ('other_types_of_sexual_abuse_or_sexual_humiliation', models.BooleanField()),
                ('knifing_or_axing', models.BooleanField()),
                ('torture', models.BooleanField()),
                ('serious_physical_injury_from_combat_situation_or_landmine', models.BooleanField()),
                ('imprisonment', models.BooleanField()),
                ('forced_labor', models.BooleanField()),
                ('extortion_or_robbery', models.BooleanField()),
                ('brainwashing', models.BooleanField()),
                ('forced_to_hide', models.BooleanField()),
                ('kidnapped', models.BooleanField()),
                ('other_forced_separation_from_family_members', models.BooleanField()),
                ('forced_to_find_and_bury_bodies', models.BooleanField()),
                ('enforced_isolation_from_others', models.BooleanField()),
                ('someone_was_forced_to_betray_you_and_place_you_at_risk', models.BooleanField()),
                ('prevented_from_burying_someone', models.BooleanField()),
                ('forced_to_desecrate_or_destroy_bodies_or_graves', models.BooleanField()),
                ('forced_to_physically_harm_family_member_or_friend', models.BooleanField()),
                ('forced_to_physically_harm_someone_who_is_not_family_or_friend', models.BooleanField()),
                ('forced_to_destroy_someone_elses_property_or_possessions', models.BooleanField()),
                ('forced_to_betray_family_member_or_friend_placing_them_at_risk', models.BooleanField()),
                ('forced_to_betray_someone_who_is_not_family_or_friend', models.BooleanField()),
                ('murder_or_death_due_to_violence_of_spouse', models.BooleanField()),
                ('murder_or_death_due_to_violence_of_child', models.BooleanField()),
                ('murder_or_death_of_other_family_member_or_friend', models.BooleanField()),
                ('disappearance_or_kidnapping_of_spouse', models.BooleanField()),
                ('disappearance_or_kidnapping_of_child', models.BooleanField()),
                ('disappearance_or_kidnapping_of_other_family_member_or_friend', models.BooleanField()),
                ('serious_injury_of_loved_one_due_to_combat_situation_or_landmine', models.BooleanField()),
                ('witness_beatings_to_head_or_body', models.BooleanField()),
                ('witness_torture', models.BooleanField()),
                ('witness_killing_or_murder', models.BooleanField()),
                ('witness_rape_or_sexual_abuse', models.BooleanField()),
                ('another_situation_that_was_very_frightening', models.BooleanField()),
                ('most_terrifying_or_hurtful_events_you_have_experienced', models.TextField(default='')),
                ('most_terrifying_or_hurtful_events_in_current_living_situation', models.TextField(default='')),
                ('beatings_to_the_head', models.BooleanField()),
                ('beatings_to_head_loss_of_consciousness', models.NullBooleanField()),
                ('beatings_to_head_if_yes_how_long', models.DurationField()),
                ('suffocation_or_strangulation', models.BooleanField()),
                ('suffocation_or_strangulation_loss_of_consciousness', models.NullBooleanField()),
                ('bsuffocation_or_strangulation_if_yes_how_long', models.DurationField()),
                ('near_drowning', models.BooleanField()),
                ('near_drowning_loss_of_consciousness', models.NullBooleanField()),
                ('near_drowning_if_yes_how_long', models.DurationField()),
                ('other_types_of_injuries_to_head', models.BooleanField()),
                ('other_types_of_injuries_to_head_loss_of_consciousness', models.NullBooleanField()),
                ('other_types_of_injuries_to_head_if_yes_how_long', models.DurationField()),
                ('normal_weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('starvation_weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('were_you_near_death_due_to_starvation', models.BooleanField()),
                ('beating_or_kicking_or_striking_with_objects', models.BooleanField()),
                ('threats_or_humiliation', models.BooleanField()),
                ('being_chained_or_tied_to_others', models.BooleanField()),
                ('exposed_to_heat_or_sun_or_strong_light', models.BooleanField()),
                ('exposed_to_rain_or_body_immersion_or_cold', models.BooleanField()),
                ('placed_in_a_sack_or_box_or_or_very_small_space', models.BooleanField()),
                ('drowning_or_submersion_of_head_in_water', models.BooleanField()),
                ('suffocation', models.BooleanField()),
                ('overexertion_or_hard_labor', models.BooleanField()),
                ('exposed_to_unhygienic_conditions_conducive_to_diseases', models.BooleanField()),
                ('blindfolding', models.BooleanField()),
                ('isolation_or_solitary_confinement_specify_how_long_in_comments', models.BooleanField()),
                ('mock_execution', models.BooleanField()),
                ('made_to_witness_others_being_tortured', models.BooleanField()),
                ('starvation', models.BooleanField()),
                ('sleep_deprivation', models.BooleanField()),
                ('suspension_from_a_rod_by_hands_and_feet', models.BooleanField()),
                ('rape_or_mutilation_of_genitalia', models.BooleanField()),
                ('burning', models.BooleanField()),
                ('beating_the_soles_of_the_feet_with_rods', models.BooleanField()),
                ('blows_to_ears', models.BooleanField()),
                ('forced_standing', models.BooleanField()),
                ('throwing_urine_or_feces_at_victims', models.BooleanField()),
                ('nontherapeutic_medicine_administration', models.BooleanField()),
                ('needles_under_toes_or_fingernails', models.BooleanField()),
                ('writing_confessions_numerous_times', models.BooleanField()),
                ('shocked_repeatedly_by_electric_instrument', models.BooleanField()),
                ('other_please_specify_in_comments', models.BooleanField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='RelativeRelationships',
            fields=[
                ('relationship_num', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('relationship_type', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person1', to='PatientPortal.Patient')),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person2', to='PatientPortal.Patient')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.RelativeRelationships')),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='q',
        ),
        migrations.RemoveField(
            model_name='patientinfo',
            name='campsite',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='PatientInfo',
        ),
        migrations.DeleteModel(
            name='Q',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
        migrations.AddField(
            model_name='patient',
            name='campsite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Sites'),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Doctors'),
        ),
        migrations.AddField(
            model_name='drug_storage',
            name='campsite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Sites'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='campsite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Sites'),
        ),
        migrations.AddField(
            model_name='doctorappointments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Doctors'),
        ),
        migrations.AddField(
            model_name='doctorappointments',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientPortal.Patient'),
        ),
    ]