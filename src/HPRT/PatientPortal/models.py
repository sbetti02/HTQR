from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import Doctor
from datetime import date
import datetime

#########
## TODO: Many of these fields shouldn't have null=True in production!
#########

#    date = models.DateField(_("Date"), default=datetime.date.today)

## TODO: Write API that runs on top of this base model layer to be able to interact
##       with the models appropriately


class Site(models.Model):
    name = models.CharField(max_length=200, null = True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null = True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null = True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)
    blood_type = models.CharField(max_length = 10, null=True)
    height = models.DecimalField(max_digits = 4, decimal_places = 1, null=True) # In centimeters
    weight = models.DecimalField(max_digits = 4, decimal_places = 1, null=True) # In kg, max_digits non-inclusive
    site = models.ForeignKey(Site, on_delete = models.CASCADE, null=True)
    allergies = models.TextField(default='', blank = True, null = True)
    current_medications = models.TextField(default='', blank = True, null = True)
    # phone_number = PhoneNumberField()
    email = models.EmailField()
    #picture = models.ImageField(upload_to="PatientPortal/profiles.py", 
    #                                     height_field=500, width_field=500, null=True)
    # TODO: fingerprints, picture

    def __str__(self):
        return self.name

    def age(self):
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))



class DocPat(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, null=True)

# class Toolkit(models.Model):
#     def answer_default():
#         return False

#     docpat = models.ForeignKey(DocPat, on_delete = models.CASCADE)
#     # patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
#     # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)

#     ask = models.BooleanField(default=answer_default)
#     identify = models.BooleanField(default=answer_default)
#     diagnose_and_treat = models.BooleanField(default=answer_default)
#     refer = models.BooleanField(default=answer_default)
#     reinforce_and_teach = models.BooleanField(default=answer_default)
#     recommend = models.BooleanField(default=answer_default)
#     reduce_high_risk_behavior = models.BooleanField(default=answer_default)
#     be_culturally_attuned = models.BooleanField(default=answer_default)
#     prescribe = models.BooleanField(default=answer_default)
#     close_and_schedule = models.BooleanField(default=answer_default)
#     prevent_burnout = models.BooleanField(default=answer_default)


# TODO: Does this still implicitly create an ID column? I don't want it to 
class RelativeRelationships(models.Model):
    relationship_num = models.PositiveSmallIntegerField(primary_key=True)
    relationship_type = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.relationship_num) + " - " + self.relationship_type


# TODO: On add/alter, add/alter reverse relationship as well
class Relatives(models.Model):
    person = models.ForeignKey(Patient, related_name="person1", on_delete=models.CASCADE)
    related_to = models.ForeignKey(Patient, related_name="person2", on_delete=models.CASCADE)
    relation = models.ForeignKey(RelativeRelationships, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name + " => " + self.related_to.name + ", " + self.relation.relationship_type



# class Questionnaire(models.Model):
#     patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     date = models.DateField()
#     lack_of_shelter = models.BooleanField()
#     lack_of_food_or_water = models.BooleanField()
#     ill_health_without_access_to_medical_care = models.BooleanField()
#     confiscation_or_destruction_of_personal_property = models.BooleanField()
#     combat_situation = models.BooleanField()
#     forced_evacuation_under_dangerous_conditions = models.BooleanField()
#     beating_to_the_body = models.BooleanField()
#     rape = models.BooleanField()
#     other_types_of_sexual_abuse_or_sexual_humiliation = models.BooleanField()
#     knifing_or_axing = models.BooleanField()
#     torture = models.BooleanField()
#     serious_physical_injury_from_combat_situation_or_landmine = models.BooleanField()
#     imprisonment = models.BooleanField()
#     forced_labor = models.BooleanField()
#     extortion_or_robbery = models.BooleanField()
#     brainwashing = models.BooleanField()
#     forced_to_hide = models.BooleanField()
#     kidnapped = models.BooleanField()
#     other_forced_separation_from_family_members = models.BooleanField()
#     forced_to_find_and_bury_bodies = models.BooleanField()
#     enforced_isolation_from_others = models.BooleanField()
#     someone_was_forced_to_betray_you_and_place_you_at_risk = models.BooleanField()
#     #someone_was_forced_to_betray_you_and_place_you_at_risk_of_death_or_injury = models.BooleanField()
#     prevented_from_burying_someone = models.BooleanField()
#     #forced_to_desecrate_or_destroy_the_bodies_or_graves_of_deceased_persons = models.BooleanField()
#     forced_to_desecrate_or_destroy_bodies_or_graves = models.BooleanField()
#     forced_to_physically_harm_family_member_or_friend = models.BooleanField()
#     forced_to_physically_harm_someone_who_is_not_family_or_friend = models.BooleanField()
#     forced_to_destroy_someone_elses_property_or_possessions = models.BooleanField()
#     #forced_to_betray_family_member_or_friend_placing_them_at_risk_of_death_or_injury = models.BooleanField()
#     forced_to_betray_family_member_or_friend_placing_them_at_risk = models.BooleanField()
#     #forced_to_betray_someone_who_is_not_family_or_friend_placing_them_at_risk_of_death_or_injury = models.BooleanField()
#     forced_to_betray_someone_who_is_not_family_or_friend = models.BooleanField()
#     murder_or_death_due_to_violence_of_spouse = models.BooleanField()
#     murder_or_death_due_to_violence_of_child = models.BooleanField()
#     murder_or_death_of_other_family_member_or_friend = models.BooleanField()
#     disappearance_or_kidnapping_of_spouse = models.BooleanField()
#     disappearance_or_kidnapping_of_child = models.BooleanField()
#     disappearance_or_kidnapping_of_other_family_member_or_friend = models.BooleanField()
#     serious_injury_of_loved_one_due_to_combat_situation_or_landmine = models.BooleanField()
#     witness_beatings_to_head_or_body = models.BooleanField()
#     witness_torture = models.BooleanField()
#     witness_killing_or_murder = models.BooleanField()
#     witness_rape_or_sexual_abuse = models.BooleanField()
#     #another_situation_that_was_very_frightening_or_in_which_you_felt_your_life_was_in_danger = models.BooleanField()
#     another_situation_that_was_very_frightening = models.BooleanField()
#     most_terrifying_or_hurtful_events_you_have_experienced = models.TextField(default='')
#     #most_terrifying_or_hurtful_events_you_have_experienced_in_current_living_situation_if_different_from_above = models.TextField(default='')
#     most_terrifying_or_hurtful_events_in_current_living_situation = models.TextField(default='')
#     beatings_to_the_head = models.BooleanField()
#     beatings_to_head_loss_of_consciousness = models.NullBooleanField()
#     beatings_to_head_if_yes_how_long = models.DurationField()
#     suffocation_or_strangulation = models.BooleanField()
#     suffocation_or_strangulation_loss_of_consciousness = models.NullBooleanField()
#     bsuffocation_or_strangulation_if_yes_how_long = models.DurationField()
#     near_drowning = models.BooleanField()
#     near_drowning_loss_of_consciousness = models.NullBooleanField()
#     near_drowning_if_yes_how_long = models.DurationField()
#     other_types_of_injuries_to_head = models.BooleanField()
#     other_types_of_injuries_to_head_loss_of_consciousness = models.NullBooleanField()
#     other_types_of_injuries_to_head_if_yes_how_long = models.DurationField()
#     starvation = models.BooleanField()
#     normal_weight = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
#     starvation_weight = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
#     were_you_near_death_due_to_starvation = models.BooleanField()

#     # recurrent_thoughts_or_memories_of_the_most_hurtful_or_terrifying_events
#     # feeling_as_though_the_event_is_happening_again
#     # recurrent_nightmares
#     # feeling_detached_or_withdrawn_from_people
#     # unable_to_feel_emotions
#     # feeling_jumpy_or_easily_startled
#     # difficulty_concentrating
#     # trouble_sleeping
#     # feeling_on_guard
#     # feeling_irritable_or_having_outbursts_of_anger
#     # avoiding_activities_that_remind_you_of_the_traumatic_or_hurtful_event
#     # inability_to_remember_parts_of_the_most_hurtful_or_traumatic_events
#     # less_interest_in_daily_activities
#     # feeling_as_if_you_don’t_have_a_future
#     # avoiding_thoughts_or_feelings_associated_with_the_traumatic_or_hurtful_events
#     # sudden_emotional_or_physical_reaction_when_reminded_of_the_most_hurtful_or_traumatic_events

#     # feeling_that_you_have_less_skills_than_you_had_before
#     # having_difficulty_dealing_with_new_situations
#     # feeling_exhausted
#     # bodily_pain
#     # troubled_by_physical_problems
#     # poor_memory
#     # finding_out_or_being_told_by_other_people_that_you_have_done_something_that_you_cannot_remember
#     # difficulty_paying_attention
#     # feeling_as_if_you_are_split_into_two_people_and_one_of_you_is_watching_what_the_other_is_doing
#     # feeling_unable_to_make_daily_plans
#     # blaming_yourself_for_things_that_have_happened
#     # feeling_guilty_for_having_survived
#     # hopelessness
#     # feeling_ashamed_of_the_hurtful_or_traumatic_events_that_have_happened_to_you
#     # feeling_that_people_do_not_understand_what_happened_to_you
#     # feeling_others_are_hostile_to_you
#     # feeling_that_you_have_no_one_to_rely_upon
#     # feeling_that_someone_you_trusted_betrayed_you
#     # feeling_humiliated_by_your_experience
#     # feeling_no_trust_in_others
#     # feeling_powerless_to_help_others
#     # spending_time_thinking_why_these_events_happened_to_you
#     # feeling_that_you_are_the_only_one_that_suffered_these_events
#     # feeling_a_need_for_revenge

#     beating_or_kicking_or_striking_with_objects = models.BooleanField()
#     threats_or_humiliation = models.BooleanField()
#     being_chained_or_tied_to_others = models.BooleanField()
#     exposed_to_heat_or_sun_or_strong_light = models.BooleanField()
#     exposed_to_rain_or_body_immersion_or_cold = models.BooleanField()
#     placed_in_a_sack_or_box_or_or_very_small_space = models.BooleanField()
#     drowning_or_submersion_of_head_in_water = models.BooleanField()
#     suffocation = models.BooleanField()
#     overexertion_or_hard_labor = models.BooleanField()
#     #exposed_to_unhygienic_conditions_conducive_to_infections_or_other_diseases = models.BooleanField()
#     exposed_to_unhygienic_conditions_conducive_to_diseases = models.BooleanField()
#     blindfolding = models.BooleanField()
#     isolation_or_solitary_confinement_specify_how_long_in_comments = models.BooleanField()
#     mock_execution = models.BooleanField()
#     made_to_witness_others_being_tortured = models.BooleanField()
#     starvation = models.BooleanField()
#     sleep_deprivation = models.BooleanField()
#     suspension_from_a_rod_by_hands_and_feet = models.BooleanField()
#     rape_or_mutilation_of_genitalia = models.BooleanField()
#     burning = models.BooleanField()
#     beating_the_soles_of_the_feet_with_rods = models.BooleanField()
#     blows_to_ears = models.BooleanField()
#     forced_standing = models.BooleanField()
#     #throwing_urine_or_feces_at_victims_or_being_made_to_throw_it_at_other_prisoners = models.BooleanField()
#     throwing_urine_or_feces_at_victims = models.BooleanField()
#     nontherapeutic_medicine_administration = models.BooleanField()
#     needles_under_toes_or_fingernails = models.BooleanField()
#     writing_confessions_numerous_times = models.BooleanField()
#     shocked_repeatedly_by_electric_instrument = models.BooleanField()
#     other_please_specify_in_comments = models.BooleanField()

#     # suddenly_scared_for_no_reason
#     # feeling_fearful
#     # faintness_or_dizziness_or_weakness
#     # nervousness_or_shakiness_inside
#     # heart_pounding_or_racing
#     # trembling
#     # feeling_tense_or_keyed_up
#     # headaches
#     # spell_of_terror_or_panic
#     # feeling_restless_or_cant_sit_still
#     # feeling_low_in_energy_or_slowed_down
#     # blaming_yourself_for_things
#     # crying_easily
#     # loss_of_sexual_interest_or_pleasure
#     # poor_appetite
#     # difficulty_falling_asleep_or_staying_asleep
#     # feeling_hopeless_about_future
#     # feeling_blue
#     # feeling_lonely
#     # thought_of_ending_your_life
#     # feeling_of_being_trapped_or_caught
#     # worry_too_much_about_things
#     # feeling_no_interest_in_things
#     # feeling_everything_is_an_effort
#     # feeling_of_worthlessness









