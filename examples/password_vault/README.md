# Local Password Vault Service

A secure, locally-deployed password storage server with end-to-end encryption.

## Features
- **Master Password Hashing**: Uses `bcrypt` for secure authentication.
- **Entry Encryption**: Uses `cryptography` (Fernet/AES) to encrypt stored secrets.
- **Local Storage**: SQLite database for portability.
- **REST API**: FastAPI-based interface for programmatic access.

## Security Architecture
1. **Master Secret**: Derived from your master password (never stored in plain text).
2. **Data-at-Rest**: All passwords in the database are encrypted using an encryption key.
3. **Session Security**: JWT-based authentication.

## Getting Started
1. Install dependencies: `pip install fastapi uvicorn cryptography bcrypt pyjwt`
2. Run the server: `python vault/app.py`
3. Access API at `http://localhost:8000`

## Project Structure
- `vault/crypto.py`: Encryption and Hashing logic.
- `vault/models.py`: Database schema and ORM.
- `vault/app.py`: FastAPI endpoints and business logic.
