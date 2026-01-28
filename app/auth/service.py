from app.core.security import hash_password, verify_password, create_access_token

fake_users_db = {}

def register_user(email: str, password: str):
    if email in fake_users_db:
        return None

    fake_users_db[email] = {
        "email": email,
        "password": hash_password(password)
    }
    return fake_users_db[email]

def authenticate_user(email: str, password: str):
    user = fake_users_db.get(email)
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    token = create_access_token({"sub": email})
    return token
