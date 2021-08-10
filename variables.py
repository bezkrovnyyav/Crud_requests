import pytest
import requests
from faker import Faker
faker = Faker()

"""The name and the email attributes are auto-generated via Faker library for the payload"""

fake_name = faker.name()
fake_mail = faker.email()

fake_name_2 = faker.name()
fake_mail_2 = faker.email()

"""Create VARIABLES for the testing"""

# AUTH is used for the making POST/PUT/DELETE requests
AUTH = "c73016c3f2fee9093e20373c607953ff1577b954fbf0570d890f36ffb10ed16c"

# payload is used in the POST request method
payload = {'name': fake_name, 'email': fake_mail, 'gender': 'female', 'status': 'active'}

# updated_payload is used in the PUT request method
update_payload = {'name': fake_name_2, 'email': fake_mail_2, 'gender': 'female', 'status': 'active'}


"""
The data after creating the new entry using the "test_creating_new_user_via_POST" request 
in the requests_test.py file is verified via the data_verification() function
"""


def data_verificate(url):
    result = requests.get(url + str(pytest.global_response_id)).json()
    if result['data']['id'] == pytest.global_response_id and \
            result['data']['name'] == fake_name and \
            result['data']['email'] == fake_mail and \
            result['data']['gender'] == "female" and \
            result['data']['status'] == "active":
        print("\nData Verification is success!")
        print(result)
        return True
    else:
        print("\nData Verification is failed!")
        return False
