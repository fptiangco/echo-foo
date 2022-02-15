from server import app

def test_foo():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'foo'