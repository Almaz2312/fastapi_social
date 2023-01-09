def test_get_dweets(client):
    response = client.get('/dweets/dashboard/')
    assert response.status_code == 200


def test_create_dweet(client, normal_user_token_headers):
    data = {'body': 'Some New Information'}
    response = client.post('/dweets/dashboard/', headers=normal_user_token_headers, json=data)
    assert response.status_code == 200
    assert response.json()['body'] == 'Some New Information'


def test_follow(client, normal_user_token_headers):
    user_data = {'username': 'testuser1', 'email': 'testuser1@nofoobar.com', 'password': 'testing'}
    client.post('/accounts/register/', json=user_data)
    data = {'following_id': 2}
    response = client.post('/dweets/follow/', json=data, headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()['following_id'] == 2


def test_get_following(client, normal_user_token_headers):
    user_data = {'username': 'testuser2', 'email': 'testuser2@nofoobar.com', 'password': 'testing'}
    client.post('/accounts/register/', json=user_data)
    data = {'following_id': 3}
    client.post('/dweets/follow/', json=data, headers=normal_user_token_headers)
    response = client.get('/dweets/follow/', headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()[1]['following_id'] == 3


def test_unfollow(client, normal_user_token_headers):
    data = {'following_id': 2}
    client.post('/dweets/follow/', json=data, headers=normal_user_token_headers)
    response = client.delete('/dweets/unfollow/2/', headers=normal_user_token_headers)
    print(response.json())
    user_cr = client.get('/accounts/profile_list/')
    print(user_cr.json())
    dw = client.get('/dweets/follow/', headers=normal_user_token_headers)
    print(dw.json())
    assert response.status_code == 200
    assert response.json()['msg'] == 'You have unfollowed user id 2'
