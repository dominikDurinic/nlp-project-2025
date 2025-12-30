from dateutil import parser

def normalize_date(date_str):
    try:
        dt = parser.parse(date_str, dayfirst=True)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return None
