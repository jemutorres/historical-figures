def test_ping(test_app) -> None:
    """
    Test the GET main method of the application
    """
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Historical Figures Repository", "environment": "dev",
                               "testing": True}
