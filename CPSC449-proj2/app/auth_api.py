import sqlite3
import sys
from pathlib import Path
sys.path.append(r"./app")

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from database import *
from auth_models import *
from register import *
from mkclaims import *
from mkjwks import *

app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/register")
def register(
    username: str,
    password: str,
    roles: str,
    auth_db: sqlite3.Connection = Depends(write_auth_db)
):
    """Register a new user."""

    # Check if the user already exists.
    cursor = auth_db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users_auth WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    cursor.close()
    if count > 0:
        raise HTTPException(status_code=409, detail="User already exists.")

    # Register the new user.
    try:
        hashed_password = hash_password(password)
        auth_db.execute(
            """
                INSERT INTO users_auth (username, password, roles)
                VALUES(?, ?, ?)
            """,
            (
                username,
                hashed_password,
                roles
            ),
        )
        auth_db.commit()
        user_id = auth_db.execute("SELECT last_insert_rowid()").fetchone()[0]
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Failed to Register User:{e}")

    # Return a success response.
    return {"message": "User registered successfully.", "user_id": user_id}


@app.get("/login")
def login(
    username: str,
    input_password: str,
    #token: Annotated[str, Depends(oauth2_scheme)],
    auth_db: sqlite3.Connection = Depends(write_auth_db)
):
    # Get users password
    try:
        cur = auth_db.cursor()
        cur.execute(
            "SELECT id, username, password, roles FROM users_auth WHERE username = ?", (username,)
        )
        user = cur.fetchone()
        user_id = user[0]
        user_name = user[1]
        password = user[2]
        roles = user[3]
        cur.close()
        print(user)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"User doesnt exist:{e}")

    # Check the user's password.
    if not verify_password(input_password, password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    jwt = generate_claims(user_name, user_id, roles)

    # Write tokens to JSON files
    if Path('./app/jwt.json').is_file():
        # Create File and Add in Public Token for Validation
        file = open("./app/jwt.json", "a")
        file.write(jwt)
    else:
        # Add in Public Token for Validation
        file = open("./app/jwt.json", "w")
        file.write(jwt)

    # Generate JWS Token
    jwks = generate_keys(str(user_id))

    if Path('./app/jwks.json').is_file():
        # Create File and Add in Private Token for Signing
        file = open("./app/jwks.json", "a")
        file.write(jwks)
    else:
        # Add in Private Token for Signing
        file = open("./app/jwks.json", "w")
        file.write(jwks)