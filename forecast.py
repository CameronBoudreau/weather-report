class TenDayForecast():
    def __init__(self, data):
        self.days = self.get_days(data)

    def get_days(self, data):
        days = []
        for i in range(0, 10):
            new_day = DayForecast(data, i)
            days.append(new_day)
        return days

    def display_forecast(self):
        for day in self.days:
            day.display_day()


class DayForecast():
    def __init__(self, data, day):
        self.day_data = data['simpleforecast']['forecastday'][day]
        self.morning = data['txt_forecast']['forecastday'][day * 2]
        self.evening = data['txt_forecast']['forecastday'][day * 2 + 1]

        self.date = ' '.join((self.day_data['date']['monthname'],
                              str(self.day_data['date']['day'])))

        self.morning_title = self.morning['title']
        self.evening_title = self.evening['title']

        self.morning_summary = self.morning['fcttext']
        self.evening_summary = self.evening['fcttext']

        self.high = self.day_data['high']['fahrenheit']
        self.low = self.day_data['low']['fahrenheit']

    def display_day(self):
        print('*' * 20 + '\n')
        print(self.morning_title, self.date)
        print('-' * 10)
        print(self.morning_summary)
        print('High: ', self.high)
        print('Low: ', self.low, '\n')
        print(self.evening_title)
        print('-' * 10)
        print(self.evening_summary, '\n\n')
