"""Test provider"""
from http import HTTPStatus


instance_provider = {
    'id': 'YVVG4AJ9920WGY9I',
    'name': 'test',
    'company': 'test 123',
    'amount_products': 1000
}


def test_post_provider(client):
    """Test API/POST provider by test"""
    response = client.post("api/v1/providers", json=instance_provider)
    assert response.status_code == int(HTTPStatus.CREATED)
    assert response.json['name'] == instance_provider['name']
    assert response.json['company'] == instance_provider['company']
    assert response.json['amount_products'] == instance_provider['amount_products']


def test_get_provider_by_id(client):
    """Test API/GET provider by dict_provider"""
    response = client.get(f"api/v1/providers/{instance_provider.get('id')}")
    assert response.status_code == int(HTTPStatus.OK)


def test_get_provider_not_found(client):
    """Test API/GET provider by dict_provider"""
    response = client.get(f"api/v1/providers/4ADW85D8WD58DA5B")
    assert response.status_code == int(HTTPStatus.NOT_FOUND)


def test_get_provider_id_invalid(client):
    """Test API/GET provider by dict_provider"""
    response = client.get(f"api/v1/providers/4ADW85D8WD58DA5B11")
    assert response.status_code == int(HTTPStatus.BAD_REQUEST)


def test_get_provider_all(client):
    """Test API/GET provider by dict_provider"""
    response = client.get("api/v1/providers")
    assert response.status_code == int(HTTPStatus.OK)


def test_put_provider(client):
    """Test API/PUT provider"""
    response = client.put(f"api/v1/providers/{instance_provider.get('id')}",
                          json={
                              'name': 'Flask App',
                              'company': 'Testing App',
                              'amount_products': 5000
                          })
    assert response.status_code == int(HTTPStatus.OK)


def test_delete_provider(client):
    """Test API/DELETE provider"""
    response = client.delete(f"api/v1/providers/{instance_provider.get('id')}")
    assert response.status_code == int(HTTPStatus.OK)


def pytest_finish(finish_test):
    """"Finish test"""
