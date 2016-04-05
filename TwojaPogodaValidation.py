# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time


'''
Created by: Marcin Sikorski
Date: 01.04.2016
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
mapDays = {"mapTommorrow":"3","MapaPojutrze":"4","MapaPoniedzialek":"5",
       "MapaDzisiaj":"1" }

def weatherResult(day, weatherTemp, temp):
    if weatherTemp == temp:
        print('\n ' + day + " temperatura zgadza się" + "\n ................")
    else:
        print('\n ' + day + " temperatura NIE ZGADZA SIE" + "\n.............")
    return

def iconResult(day, iconTodayOnMap, iconTodayInSquare):
    if iconTodayInSquare.lower() == iconTodayOnMap:
        print("\n" + day + " pogoda zgadza się" + "\n ................")
    else:
        print("\n" + day + "pogoda NIE ZGADZA SIE" + "\n ................")
    return
'''
def tempOnMap():
    driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[1]/p[2]/span").text \
    + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[" \
    + "2]/div[1]/p[2]/sup").text + "\n" + square
'''

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

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
            str(mapDayId) + "]/a").click()
        time.sleep(1)

        tempOnMap = self.driver.find_element_by_id( self.findCityId() ).text
        print("tempOnMap: " + tempOnMap)

        tempOnBoxInfo = self.getTempOnBoxInfo( boxInfoDayId )
        print("tempOnBoxInfo: " + tempOnBoxInfo)

        if( tempOnMap == tempOnBoxInfo ):
            return True
        else:
            return False

    def getTempOnBoxInfo(self, dayId):
            driver = self.driver
            tempOnBoxInfo = driver.find_element_by_xpath(
                ".//*["
                "@id='box-info-tab3']/div[2]/div[" + str(dayId) + "]/p["
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

        #self.onMap = self.findCity()
        #print(self.onMap)

        assert( self.validateTemp(3, 1) )
        assert( self.validateTemp(4, 2) )
        assert( self.validateTemp(5, 3) )
        #assert( self.validateTemp(1, 1) )



        return


        ###########################################################################################



        #tempTomorrow = tempOnMap()
        tempTomorrow = 23
        print(tempTomorrow)

        weatherResult("Jutro", tomorrowWeather, tempTomorrow)

        iconTomorrow = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[1]/img").get_attribute(
            "title")
        print(iconTomorrow.lower())

        iconOnMap = driver.find_element_by_xpath(
            "//a[@id='" + onMap + "']/img").get_attribute("title")
        print(iconOnMap)

        iconResult("Jutrzejsza", iconOnMap, iconTomorrow)

        ###########################################################################################
        MapaPojutrze = driver.find_element_by_xpath(
            ".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[4]/a").click()
        time.sleep(1)





        #Temp. pojutrze na mapie
        tempNaStroniePojutrze = driver.find_element_by_id(onMap)
        pogodaPojutrze = tempNaStroniePojutrze.text
        print(pogodaPojutrze)

        #Temp. pojutrze w kwadracie
        TempPojutrze = self.getTemp(2)
        '''
        TempPojutrze = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[2]/p[2]/span").text + " " + driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[2]/p[2]/sup").text + "\n" + square
        print(TempPojutrze)
'''
        weatherResult("Pojutrze", pogodaPojutrze, TempPojutrze)


        #Ikona z kwadratu pojutrze
        ikonaPojutrze = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[2]/img").get_attribute(
            "title")
        print(ikonaPojutrze.lower())

        #Ikona z mapy pojutrze
        naStroniePojutrzeIkona = driver.find_element_by_xpath(
            "//a[@id='" + onMap + "']/img").get_attribute("title")
        print(naStroniePojutrzeIkona)

        iconResult("Pojutrze", naStroniePojutrzeIkona, ikonaPojutrze)

        ###########################################################################################
        #kliknij Poniedziałek
        MapaPoniedzialek = driver.find_element_by_xpath(
            ".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[5]/a").click()
        time.sleep(1)

        #Temp. w poniedzialek na mapie
        naStroniePoniedzialek = driver.find_element_by_id(onMap)
        pogodaPopojutrze = naStroniePoniedzialek.text
        print(pogodaPopojutrze)

        #Temp. w poniedzialek w kwadracie
        tempPoniedzialek = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[3]/p[2]/span").text + " " + driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[3]/p[2]/sup").text + "\n" + square
        print(tempPoniedzialek)



        weatherResult("W poniedzialek", pogodaPopojutrze, tempPoniedzialek)

        #Ikona z kwadratu w poniedzialek
        ikonaPoniedzialek = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[2]/div[3]/img").get_attribute(
            "title")
        print(ikonaPoniedzialek.lower())

        #Ikona z mapy w poniedzialek
        naStroniePoniedzialekIkona = driver.find_element_by_xpath(
            "//a[@id='" + onMap + "']/img").get_attribute("title")
        print(naStroniePoniedzialekIkona)

        iconResult("W poniedzialek", naStroniePoniedzialekIkona, ikonaPoniedzialek)

        ###########################################################################################
        #kliknij dzisiaj na mapie
        MapaDzisiaj = driver.find_element_by_xpath(
            ".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[1]/a").click()
        time.sleep(1)

        #temp na mapie dzisiaj
        tempNaStronieDzis = driver.find_element_by_id(onMap)
        pogodaDzis = tempNaStronieDzis.text
        print(pogodaDzis)

        #Temp. w kwadracie dzisiaj
        TempDzis = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[1]/div/p[2]/span").text + " " + driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[1]/div/p[2]/sup").text + "\n" + square
        print(TempDzis)

        weatherResult("Dzis", pogodaDzis, TempDzis)

        #Ikona z kwadratu dzisiaj
        ikonaDzis = driver.find_element_by_xpath(
            ".//*[@id='box-info-tab3']/div[1]/img").get_attribute("title")
        print(ikonaDzis.lower())

        #Ikona z mapy dzisiaj
        naStronieDzisIkona = driver.find_element_by_xpath(
            "//a[@id='" + onMap + "']/img").get_attribute("title")
        print(naStronieDzisIkona)

        iconResult("Dzisiaj ", naStronieDzisIkona, ikonaDzis)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
