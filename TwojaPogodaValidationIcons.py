
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

        self.dayOnMap = {'today': 1,
                    'tommorow': 3,
                    'dayafter': 4,
                    'dayafterafter': 5}

        self.dayOnBoxInfo = {'today': 'div[1]/img',
                    'tommorow': 'div[2]/div[1]/img',
                    'dayafter': 'div[2]/div[2]/img',
                    'dayafterafter': 'div[2]/div[3]/img'}

    def findCity(self):
        return self.driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[1]/div/p[1]").text

    def findCityId(self):
        cityMap = {'Szczecin': 'map-city-972', 'Koszalin': 'map-city-773',
                'Gdańsk': 'map-city-2030', 'Olsztyn': 'map-city-1067',
                'Suwałki': 'map-city-1918', 'Zielona Góra': 'map-city-1628',
                'Poznań': 'map-city-294', 'Bydgoszcz': 'map-city-1069',
                'Warszawa': 'map-city-2333', 'Białystok': 'map-city-491',
                'Wrocław': 'map-city-2517', 'Opole': 'map-city-2281',
                'Łódź': 'map-city-1176', 'Kielce': 'map-city-1142',
                'Lublin': 'map-city-1294', 'Katowice': 'map-city-1082',
                'Kraków': 'map-city-2074', 'Rzeszów': 'map-city-625'}

        city = self.findCity()
        assert(city in cityMap)
        cityId = cityMap[city]
        return cityId

    def getWeatherOnMap(self):
        return self.driver.find_element_by_xpath(
            "//a[@id='" + str(self.findCityId()) + "']/img").get_attribute(
            "title")

    def getWeatherOnBoxInfo(self, dayId):
        driver = self.driver
        weatherOnBoxInfo = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/" + dayId
            ).get_attribute("title")
        return weatherOnBoxInfo.lower()

    def validateWeather(self, mapDayId, boxInfoDayId):
        self.driver.find_element_by_xpath(".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[" +
            str(self.dayOnMap[mapDayId]) + "]/a").click()

        time.sleep(1)

        weatherOnMap = self.getWeatherOnMap()
        print("WeatherOnMap: " + weatherOnMap)

        weatherOnBoxInfo = self.getWeatherOnBoxInfo( self.dayOnBoxInfo[boxInfoDayId] )
        print("tempWeatherOnBoxInfo: " + weatherOnBoxInfo)

        if( weatherOnMap == weatherOnBoxInfo ):
            return True
        else:
            return False

    def test(self):
        driver = self.driver
        actionChains = self.actionChains

        driver.get("http://www.twojapogoda.pl/")
        driver.maximize_window()
        time.sleep(1)

        assert( self.validateWeather('today', 'today'))
        assert( self.validateWeather('tommorow', 'tommorow'))
        assert( self.validateWeather('dayafter', 'dayafter'))
        assert( self.validateWeather('dayafterafter', 'dayafterafter'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
