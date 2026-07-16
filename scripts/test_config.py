from app.core.config import settings

print("=" * 40)
print("Application Configuration")
print("=" * 40)

print(f"App Name        : {settings.app_name}")
print(f"Environment     : {settings.environment}")
print(f"Database Host   : {settings.database_host}")
print(f"Database Port   : {settings.database_port}")
print(f"Database Name   : {settings.database_name}")