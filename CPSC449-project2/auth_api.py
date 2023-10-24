import sqlite3

from fastapi import FastAPI, Depends, HTTPException
from database import get_auth_db
from model_requests import RegisterUserRequest

from auth_models import *
from register import *
from mkclaims import *

app = FastAPI()


@app.post("/register")
def register(
    user: RegisterUserRequest, auth_db: sqlite3.Connection = Depends(get_auth_db)
):
    """Register a new user."""

    # Check if the user already exists.
    cursor = auth_db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (user.username,))
    count = cursor.fetchone()[0]
    cursor.close()
    if count > 0:
        raise HTTPException(status_code=409, detail="User already exists.")

    # Register the new user.
    try:
        hashed_password = hash_password(user.password)
        auth_db.execute(
            """
                INSERT INTO users_auth (username, password, roles)
                VALUES(?, ?, ?)
            """,
            (
                user.username,
                hashed_password,
                user.roles,
            ),
        )
        auth_db.commit()
        user_id = auth_db.execute("SELECT last_insert_rowid()").fetchone()[0]
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Failed to Register User:{e}")

    # Return a success response.
    return {"message": "User registered successfully.", "user_id": user_id}


@app.post("/login")
def login(
    user: User,
    verify_password: str,
    auth_db: sqlite3.Connection = Depends(get_auth_db),
):
    # Get users password
    try:
        cursor = auth_db.cursor()
        cursor.execute(
            "SELECT password FROM users_auth WHERE username = ?", (user.username,)
        )
        password = cursor.fetchone()[0]
        cursor.close()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"User doesnt exist:{e}")

    # Check the user's password.
    if not verify_password(verify_password, password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    token = generate_claims(user.username, user.id, user.roles)
    # Return a success JWT token.
    return {"token": token}
