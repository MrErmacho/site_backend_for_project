#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Убедитесь, что путь правильно указывает на ваш файл настроек
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.configs.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        )
    execute_from_command_line(sys.argv)