import re
from datetime import datetime

def extract_date(text):
    patterns = [r"\d{4}-\d{2}-\d{2}", r"\d{1,2}\s\w{3}\s\d{2,4}"]
    for p in patterns:
        m=re.search(p,text)
        if m: return m.group()
    return None

def extract_time(text):
    m=re.search(r"\d{1,2}:\d{2}",text)
    return m.group() if m else None

def parse_ticket(text):
    return {
        "date": extract_date(text),
        "time": extract_time(text)
    }
