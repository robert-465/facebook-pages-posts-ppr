thonfrom datetime import datetime

class DateFilter:
    def __init__(self, start_date, end_date):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    def is_within_date_range(self, timestamp):
        post_date = datetime.utcfromtimestamp(timestamp / 1000)
        if self.start_date and post_date < self.start_date:
            return False
        if self.end_date and post_date > self.end_date:
            return False
        return True