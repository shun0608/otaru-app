import pytest


@pytest.mark.asyncio
async def test_register_new_account_register_user_return_success_json(async_client):
    response = await async_client.post(
        "/register",
        json={"name": "test_user", "email": "test@test.jp", "password": "password"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "email": "test@test.jp",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "name": "test_user",
    }
