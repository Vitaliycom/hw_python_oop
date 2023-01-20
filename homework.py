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
        #today_stats = sum(record.amount for record in self.records if record.date == today)
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



# создадим калькулятор денег с дневным лимитом 1000
# cash_calculator = CashCalculator(1000)
# cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="20.01.2023"))
#print(cash_calculator.get_today_cash_remained("usd"))
# должно напечататься
# На сегодня осталось 555 руб
#print(cash_calculator.get_week_stats())

calories_calculator = CaloriesCalculator(2415)
calories_calculator.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.", date="20.01.2023"))
calories_calculator.add_record(Record(amount=84, comment="Йогурт.", date="20.01.2023"))
calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов.", date="20.01.2023"))

print(calories_calculator.get_calories_remained())


