# HTQR

__Implemented__

We created an electronic version of a set of diagnostic tools used to train/guide doctors on how to communicate with and diagnose patients, refugees, suffering from trauma. Doctors can keep an a checklist (the 11-Point Toolkit) on a patient's progress. Doctors can create patient profiles which consist of some basic info (i.e. name, DOB, height, blood type, allergies, medication, phone number) and most importantly the 11-Point Toolkit. When a doctor sees a patient's profile, he/she can access the 11-Point Toolkit specific to that doctor-patient relationship. One of the most important elements of the toolkit is the screening tools found under "Diagnose" which aid in communicating a patient's circumstances and overall improving the care a doctor can provide to the patient. Any doctor can keep track of his/her progress with a patient, and in any new doctor-patient relationship, the doctor must go through all the steps in the 11-Point Toolkit. This ensure doctors ar guided throught the process every time in order to get a better understanding of each patient's circumstances. There is also a feature which allows a doctor to ask for a patient's trauma story through text once the patient's number is verified. Patient's are able to share their trauma story if they wish and add it to their patient profile. 

Sofware Requirements: django 2, Python 3, Bootstrap 4, postgresql, twilio

To run:
Download files
Go into file directory ./src/HPRT/
Then run
>python manage.py makemigrations
>python manage.py migrate
>python manage.py runserver
"Starting development server at http://127.0.0.1:8000/"

__Future Work__

In the future, we hope to have a completed analytics component which will allow a user to query the database of patients in order to observe any underlying trends among the patients. We also have plans to take our system and use it in refugee camps. 

We are working to create a way for doctors to store and retrieve patient information on refugees in refugee camps with limited access to the internet. Limited access to internet makes it harder for doctors to retrieve and share patient information. We've devised a local area network using Raspberry Pi's to retrieve and update info when internet connection is available and store, edit and share info when internet connection isn't available. We hope to implement and test such a system in the future. 

With this local area network in place, if a refugee were to move from one camp to another, we hope that patient information can be shared automatically between doctors in refugee camps.  This way, the refugees would not have to repeatedly give their personal health information and potentially details on traumatizing events in their lives.

Once we have our analytics component in place, we would like to compile healthcare statistics for refugees worldwide and on an area-by-area level as well. We want to use this data to create models or look for patterns, and be able to use that information to alert people to potential risks.  One potential focus in this aspect is human trafficking. One idea would be to use the data to try to determine particular individuals that may be more or less at risk, and have people in the camp be able to reach out to them and help them.

# Team and Sponsor Details

Our names are Scott Bettigole, Azmina Karukappadath, and Anthony Ong, and we are team Unmellow Yellow from the Tufts University Senior Capstone course.

Our direct sponsor is Dr. Karen Panetta, the Dean of Graduate Education and School of Enginnering at Tufts University.  Together, we are working to aid Dr. Richard Mollika and his team from the Harvard Medical School.
