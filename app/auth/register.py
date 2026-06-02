@router.post("/register")
def register(user: UserRegister):

    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    fake_users_db[user.username] = hashed_password

    return {
        "message": "User registered successfully"
    }