from app import create_app

def test_dashboard():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Finance Advisor" in response.data
