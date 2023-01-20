import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today = dt.datetime.now().date()
        today_stats = 0
        for record in self.records:
            if record.date == today:
                today_stats += record.amount
        return today_stats
    def get_week_stats(self):
        today = dt.datetime.now().date()
        week_date  = today - dt.timedelta(days=7)
        week_stats = 0
        for record in self.records:
            if week_date < record.date <= today:
                week_stats += record.amount
        return week_stats
    def remained(self):
        return self.limit - self.get_today_stats()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.remained()
        if calories_remained <= 0:
            return f"Хватит есть!"
        else:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"            

class CashCalculator(Calculator):
    USD_RATE = 50.7
    EURO_RATE = 60.2
    RUB_RATE = 1.0
    def get_today_cash_remained(self, currency):
        today_cash_remained = self.remained()

        if today_cash_remained == 0:
            return "Денег нет, держись"

        currencies = {
            "usd": ( self.USD_RATE, "USD"),
            "eur": ( self.EURO_RATE, "Euro"),
            "rub": ( self.RUB_RATE, "руб")
        }

        if currency not in currencies:
            return "Указана неверная валюта"

        rate, sign = currencies.get(currency)
        today_cash_remained = round(today_cash_remained / rate, 2)

        if today_cash_remained > 0:
            return f"На сегодня осталось {today_cash_remained} {sign}"

        today_cash_remained = -today_cash_remained
        return f"Денег нет, держись: твой долг - {today_cash_remained} {sign}"

class Record:
    def __init__(self, amount, comment, date=""):
        self.amount = amount
        if date == "":
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment