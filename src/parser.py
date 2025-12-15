import json
import re
from datetime import datetime
from pathlib import Path


def _safe_match(patterns, text):
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group().strip()
    return None


def extract_date(text):
    # Regex patterns cover ISO, slash, dot, and textual month formats
    patterns = [
        r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b",
        r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b",
        r"\b\d{1,2}\s?[A-Za-z]{3,9}\s?\d{2,4}\b",
    ]
    date_str = _safe_match(patterns, text)
    if date_str:
        return date_str

    # Fallback: try to parse tokens that look like dates
    for token in text.split():
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%d/%m/%y"):
            try:
                return datetime.strptime(token, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
    return None


def extract_time(text):
    patterns = [
        r"\b\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?\b",
        r"\b\d{1,2}\s?(?:AM|PM|am|pm)\b",
        r"\b\d{3,4}\s?(?:AM|PM|am|pm)\b",  # compact times like 0730PM
    ]
    return _safe_match(patterns, text)


def extract_seat(text):
    patterns = [
        r"\b(?:Seat|Row)?\s*[A-Z]{1,3}\d{1,3}\b",
        r"\b[A-Z]{1,3}-?\d{1,3}\b",
    ]
    return _safe_match(patterns, text)


def extract_screen(text):
    patterns = [r"\b(?:Screen|Audi|Auditorium)\s*\d+\b"]
    return _safe_match(patterns, text)


def extract_movie_name(text):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return None

    ignore_patterns = [
        r"\b(Screen|Audi|Auditorium)\s*\d+\b",
        r"\bSeat\b|\bRow\b",
        r"\d{1,2}:\d{2}",
        r"\d{4}[-/]\d{1,2}[-/]\d{1,2}",
        r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}",
    ]

    def is_meta(line):
        return any(re.search(p, line, flags=re.IGNORECASE) for p in ignore_patterns)

    def is_numeric_only(line):
        return line.replace(" ", "").isdigit()

    candidates = [ln for ln in lines if not is_meta(ln) and not is_numeric_only(ln) and len(ln) > 3]
    if candidates:
        candidates.sort(key=lambda s: (-len(s), s))
        return candidates[0]
    return lines[0] if lines else None


def parse_ticket(text):
    text = text or ""
    try:
        parsed = {
            "movie_name": extract_movie_name(text),
            "date": extract_date(text),
            "time": extract_time(text),
            "seat": extract_seat(text),
            "screen": extract_screen(text),
            "raw_text": text.strip(),
        }
    except Exception:
        parsed = {
            "movie_name": None,
            "date": None,
            "time": None,
            "seat": None,
            "screen": None,
            "raw_text": text.strip(),
        }
    return parsed


def save_parsed_ticket(text, identifier=None, output_dir="parsed"):
    parsed = parse_ticket(text)
    ident = identifier or "ticket"
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    file_path = output_path / f"{ident}.json"
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
    return str(file_path)
