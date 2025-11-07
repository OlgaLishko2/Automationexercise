

def test_create_user_missing_field():
    payload = TEST_USER.copy()
    payload.pop("email")  # Remove required field
    response = create_user(payload)
    assert response.status_code == 200  # Bad request
    data = response.json()
    assert "error" in data


def test_verify_login_success():
    # Make sure user exists
    create_user(TEST_USER)
    response = verify_login(TEST_USER["email"], TEST_USER["password"])
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == "User exists!"


def test_verify_login_invalid_credentials():
    response = verify_login("wrong@example.com", "nopass")
    assert response.status_code == 404
    data = response.json()
    assert data.get("message") == "User not found!"


def test_delete_user():
    create_user(TEST_USER)
    response = delete_user(TEST_USER["email"], TEST_USER["password"])
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == "Account deleted!"

