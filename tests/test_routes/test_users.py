def test_create_user(client):
    data = {'username': 'testuser', 'email': 'testuser@nofoobar.com', 'password': 'testing'}
    response = client.post('/accounts/register/', json=data)
    assert response.status_code == 200
    assert response.json()['email'] == 'testuser@nofoobar.com'
    assert response.json()['is_active'] is True


def test_profile(client, normal_user_token_headers):
    response = client.get('/accounts/profile/', headers=normal_user_token_headers)
    assert response.json()['username'] == 'test@example.com'


def test_profiles(client, normal_user_token_headers):
    response = client.get('/accounts/profile_list/')
    assert response.status_code == 200
    assert response.json()[1]['username'] == 'test@example.com'
    assert response.json()[0]['username'] == 'testuser'
