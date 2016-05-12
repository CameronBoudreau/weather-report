import requests


class DataGrabber():
    def __init__(self):
        self.url = 'http://api.wunderground.com/api/'
        self.key = '167bacfb55bf6c78/'
        self.features = 'alerts/astronomy/conditions/currenthurricane/forecast10day/'

    def grab(self, zipcode):
        response = requests.get('{}{}{}q/{}.json'.format(self.url,
                                                         self.key,
                                                         self.features,
                                                         zipcode))
        data = response.json()
        return data
