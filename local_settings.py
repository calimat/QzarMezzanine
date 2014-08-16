
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "b257a605-c997-44b3-a027-f93b0b9a7c662c718f27-4781-418f-a97b-1acac9eb259300067a40-a9cc-41e4-9d11-88113bd86b4f"
NEVERCACHE_KEY = "5e5b9212-8556-409f-8634-f4442ad4dfb526781a8c-2e0d-45f1-9106-490b4b79fd08ae4205e5-f960-45cb-825e-f7d2fbcf7dfd"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
