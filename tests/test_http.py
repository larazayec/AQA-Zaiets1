import pytest # type: ignore
import requests # type: ignore


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Server response {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers
    
    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404
    
