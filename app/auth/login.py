@router.post("/login")
def login(user: UserLogin):

    stored_password = fake_users_db.get(user.username)

    if not stored_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }