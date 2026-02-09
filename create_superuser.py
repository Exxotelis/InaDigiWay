import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InaDigi.settings")
django.setup()

from django.contrib.auth import get_user_model  # noqa: E402


def main():
    username = os.getenv("DJANGO_SUPERUSER_USERNAME")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

    if not username or not email or not password:
        print("Superuser env vars not set; skipping.")
        return

    User = get_user_model()
    if User.objects.filter(username=username).exists():
        print("Superuser already exists; skipping.")
        return

    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")


if __name__ == "__main__":
    main()
