from dateutil import parser

HR_MONTHS = {
    "siječnja": "01",
    "veljače": "02",
    "ožujka": "03",
    "travnja": "04",
    "svibnja": "05",
    "lipnja": "06",
    "srpnja": "07",
    "kolovoza": "08",
    "rujna": "09",
    "listopada": "10",
    "studenoga": "11",
    "prosinca": "12"
}

def normalize_date(date_str):
    if not date_str:
        return None

    # 1) zamijeni hrvatske mjesece brojevima
    lower = date_str.lower()
    for hr, num in HR_MONTHS.items():
        if hr in lower:
            lower = lower.replace(hr, num)

    # sada npr. "11. veljače 2018. 15:16" postaje "11. 02 2018. 15:16"

    # 2) pokušaj parsirati
    try:
        dt = parser.parse(lower, dayfirst=True)
        return dt.strftime("%Y-%m-%d")
    except:
        return None
