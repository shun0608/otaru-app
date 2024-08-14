import pytest


@pytest.mark.asyncio
async def test_login_user(async_client):
    await async_client.post(
        "/register",
        json={"name": "test_user", "email": "test@test.jp", "password": "password"},
    )
    response = await async_client.post(
        "/login",
        content="username=test@test.jp&password=password",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 204
