import app

def test_valid_year():
    client = app.app.test_client()
    response = client.post("/", data={"birth_year": 2000})
    assert response.status_code == 200
    assert b"Tuoi" or b"tuoi"

def test_invalid_year():
    client = app.app.test_client()
    response = client.post("/", data={"birth_year": 1900})
    assert response.status_code == 200
