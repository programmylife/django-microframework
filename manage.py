from django.core.management import execute_from_command_line
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")
    execute_from_command_line()
