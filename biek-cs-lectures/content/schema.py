"""Shared checks for lecture records."""

REQUIRED = (
    "id",
    "number",
    "title",
    "kicker",
    "unit",
    "domain",
    "periods",
    "intro",
    "outcomes",
    "blocks",
    "terms",
    "checks",
    "mcqs",
    "shorts",
    "longs",
    "labs",
    "summary",
)


def lecture(**kwargs):
    missing = [key for key in REQUIRED if key not in kwargs]
    if missing:
        raise KeyError(f"{kwargs.get('id', '?')} missing {missing}")
    return kwargs
