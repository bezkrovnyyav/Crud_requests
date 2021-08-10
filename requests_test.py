import pytest
import requests
import variables



def test_checke_endpoint_activation(url):
    response = requests.get(url).json()
    assert response['code'] == 200



def test_creating_new_user_via_POST(url, token_auth):
    response = requests.post(url, headers=token_auth, data=variables.payload)
    response_json = response.json()
    response_id = response_json['data']['id']
    pytest.global_response_id = response_id 
    print("\nThe userID generated is:" + str(response_id))
    assert response_json['code'] == 201
    assert variables.data_verificate(url)  # checking creation of the data



def test_fetching_existing_user_via_GET(url):
    response = requests.get(url + str(pytest.global_response_id)).json()
    assert response['code'] == 200
    print("\nThe HTTP response code is " + str(response['code']))



def test_updating_existing_user_via_PUT(url, token_auth):
    response = requests.put(url + str(pytest.global_response_id), headers=token_auth, data=variables.update_payload)
    response_json = response.json()
    assert response_json['code'] == 200

    """ If the data_verificate() fails here, it means the user ID is updated successfully"""

    if not (variables.data_verificate(url)):
        print("The user details is updated successfully!")
        print(response_json)
        assert True
    else:
        print("The user details isn't updated!")
        assert False



def test_deleting_existing_user_via_DELETE(url, token_auth):
    response = requests.delete(url + str(pytest.global_response_id), headers=token_auth).json()
    assert response['code'] == 204 and response['data'] is None

    """After the DELETE request is executed, we should verify the 404 response code 
        via making a GET request"""

    get_response = requests.get(url + str(pytest.global_response_id)).json()
    assert get_response['code'] == 404 and \
           get_response['data']['message'] == "Resource not found"
    print("\nThe HTTP response code  is " + str(get_response['code']) + "!" +
          "\nThe user is deleted successfully!")
