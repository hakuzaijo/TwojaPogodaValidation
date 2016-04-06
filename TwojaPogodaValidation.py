# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time


'''
Created by: Marcin Sikorski
Date: 05.04.2016
--------------------------------------
Requirements: Firefox 42.0 or lower (it might not work on firefox 43 and higher)
-----------------------------------------
Case:
Test case to validate temperature and weather icons on www.twojapogoda.pl for tomorrow, the day after tomorrow, monday and today
----------------
BDD:
Given I open www.twojapogoda.pl
When I press Jutro
Then weather and icon for tomorrow on Weather map shows the same values as on Weather panel

Given I open www.twojapogoda.pl
When I press Pojutrze
Then weather and icon for the day after tomorrow on Weather map shows the same values as on Weather panel

Given I open www.twojapogoda.pl
When I press Poniedzialek
Then weather and icon for Monday on Weather map shows the same values as on Weather panel

Given I open www.twojapogoda.pl
When I press Dzis
Then weather and icon for today on Weather map shows the same values as on Weather panel
-----------------
Comments:
* Just open script in PyCharm and start by pressing shift+F10
* Sometimes script starts slowly (depends on internet connection) but it WILL start.
'''

webpage = "http://www.twojapogoda.pl/"



class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

        self.dayOnMap = {'today': 1,
                    'tommorow': 3,
                    'dayafter': 4,
                    'dayafterafter': 5}

        self.dayOnBoxInfo = {'today': 'div[1]/div/',
                    'tommorow': 'div[2]/div[1]/',
                    'dayafter': 'div[2]/div[2]/',
                    'dayafterafter': 'div[2]/div[3]/'}

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

    def validateTemp(self, mapDayId, boxInfoDayId):
        self.driver.find_element_by_xpath(
            ".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[" +
            str(self.dayOnMap[mapDayId]) + "]/a").click()
        time.sleep(1)

        tempOnMap = self.getTempOnMap()
        print("tempOnMap: " + tempOnMap)

        tempOnBoxInfo = self.getTempOnBoxInfo( self.dayOnBoxInfo[boxInfoDayId] )
        print("tempOnBoxInfo: " + tempOnBoxInfo)

        if( tempOnMap == tempOnBoxInfo ):
            return True
        else:
            return False

    def getTempOnMap(self):
        return self.driver.find_element_by_id( self.findCityId() ).text

    def getTempOnBoxInfo(self, dayId):
            driver = self.driver
            tempOnBoxInfo = driver.find_element_by_xpath(
                ".//*["
                "@id='box-info-tab3']/" + str(dayId) + "/p["
                                                            "2]/span").text \
                + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[" \
                + "2]/div[1]/p[2]/sup").text + "\n" + self.findCity()
            return tempOnBoxInfo

    def test_search_moje(self):
        driver = self.driver
        actionChains = self.actionChains

        driver.get(webpage)
        driver.maximize_window()
        time.sleep(1)

        assert( self.validateTemp('today', 'today'))
        assert( self.validateTemp('tommorow', 'tommorow'))
        assert( self.validateTemp('dayafter', 'dayafter'))
        assert( self.validateTemp('dayafterafter', 'dayafterafter'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
