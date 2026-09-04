from app.auth.password import (
    hash_password,
    verify_password,
)

password = "Admin@123"

hashed = hash_password(password)

print("Original :", password)
print("Hash     :", hashed)

print(
    verify_password(
        "Admin@123",
        hashed,
    )
)

print(
    verify_password(
        "WrongPassword",
        hashed,
    )
)