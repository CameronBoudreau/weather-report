from data_grabber import *
from conditions import *
from forecast import *


def main():
    zipcode = input("Enter your zipcode: ")

    grabber = DataGrabber()
    data = grabber.grab(zipcode)

    conditions = Conditions(data['current_observation'])
    forecast = TenDayForecast(data['forecast'])

    conditions.display_conditions()
    forecast.display_forecast()

if __name__ == '__main__':
    main()
