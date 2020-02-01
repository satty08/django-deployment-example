import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
import django
django.setup()

#fake pop script
import random
from AppTwo.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for user in range(N):
        fake_name = fake.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()

        #create new entry
        user = User.objects.get_or_create(fname= fake_first_name,
                                          lname = fake_last_name,
                                          email = fake_email)[0]

if __name__=='__main__':
    print ("Populating Data!")
    populate(15)
    print ("Populating complete")