import os
import sys
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except Exception as e:
        raise ImportError() from e
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
