""""Allow running SAGE as `python -m sage`."""

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())
