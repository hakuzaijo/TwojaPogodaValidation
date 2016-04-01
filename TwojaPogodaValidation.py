# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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
* Test saves print screen of webpage if error occurs. File is saved in folder in which script was triggered
* Sometimes script starts slowly (depends on internet connection) but it WILL start.
'''

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

    def test_search_moje(self):
        driver = self.driver
        actionChains = self.actionChains

        ###########################################################################################
        driver.get("http://www.twojapogoda.pl/")
        driver.maximize_window()
        time.sleep(1)

        city = {'Szczecin':'map-city-972','Koszalin':'map-city-773','Gdańsk':'map-city-2030','Olsztyn':'map-city-1067','Suwałki':'map-city-1918','Zielona Góra':'map-city-1628','Poznań':'map-city-294','Bydgoszcz':'map-city-1069','Warszawa':'map-city-2333','Białystok':'map-city-491','Wrocław':'map-city-2517','Opole':'map-city-2281','Łódź':'map-city-1176','Kielce':'map-city-1142','Lublin':'map-city-1294','Katowice':'map-city-1082','Kraków':'map-city-2074','Rzeszów':'map-city-625'}
        bok = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[1]/div/p[1]").text
        #print(bok)

        if bok in city:
            naMapie = (city[bok])
            #print(city[bok])

        ###########################################################################################
        #kliknij jutro na mapie
        MapaJutro = driver.find_element_by_xpath(".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[3]/a").click()
        time.sleep(1)

        #temp. na mapie jutro
        tempNaStronieJutro = driver.find_element_by_id(naMapie)
        pogodaJutro = tempNaStronieJutro.text
        print(pogodaJutro)

        #temp. w kwadracie na jutro
        tempJutro = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[1]/p[2]/span").text + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[1]/p[2]/sup").text + "\n" + bok
        print(tempJutro)

        if tempJutro == pogodaJutro:
            print("\nJutrzejsza temperatura zgadza się")
            print(".............................")
        else:
            print("\nJutrzejsza temperatura NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        #Ikona z kwadratu na jutro
        ikonaJutro = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[1]/img").get_attribute("title")
        print(ikonaJutro.lower())

        #Ikona z mapy na jutro
        naStronieJutroIkona = driver.find_element_by_xpath("//a[@id='"+naMapie+"']/img").get_attribute("title")
        print(naStronieJutroIkona)

        if ikonaJutro.lower() == naStronieJutroIkona:
            print("\nJutrzejsza pogoda zgadza się")
            print(".............................")
        else:
            print("\nJutrzejsza pogoda NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return
        ###########################################################################################
        #kliknij pojutrze na mapie
        MapaPojutrze = driver.find_element_by_xpath(".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[4]/a").click()
        time.sleep(1)

        #Temp. pojutrze na mapie
        tempNaStroniePojutrze = driver.find_element_by_id(naMapie)
        pogodaPojutrze = tempNaStroniePojutrze.text
        print(pogodaPojutrze)

        #Temp. pojutrze w kwadracie
        TempPojutrze = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[2]/p[2]/span").text + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[2]/p[2]/sup").text + "\n" + bok
        print(TempPojutrze)

        if TempPojutrze == pogodaPojutrze:
            print("\nPojutrze temperatura zgadza się")
            print(".............................")
        else:
            print("\nPojutrze temperatura NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        #Ikona z kwadratu pojutrze
        ikonaPojutrze = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[2]/img").get_attribute("title")
        print(ikonaPojutrze.lower())

        #Ikona z mapy pojutrze
        naStroniePojutrzeIkona = driver.find_element_by_xpath("//a[@id='"+naMapie+"']/img").get_attribute("title")
        print(naStroniePojutrzeIkona)

        if ikonaPojutrze.lower() == naStroniePojutrzeIkona:
            print("\nPojutrze pogoda zgadza się")
            print(".............................")
        else:
            print("\nPojutrze pogoda NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        ###########################################################################################
        #kliknij Poniedziałek
        MapaPoniedzialek = driver.find_element_by_xpath(".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[5]/a").click()
        time.sleep(1)

        #Temp. w poniedzialek na mapie
        naStroniePoniedzialek = driver.find_element_by_id(naMapie)
        pogodaPopojutrze = naStroniePoniedzialek.text
        print(pogodaPopojutrze)

        #Temp. w poniedzialek w kwadracie
        tempPoniedzialek = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[3]/p[2]/span").text + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[3]/p[2]/sup").text + "\n" + bok
        print(tempPoniedzialek)

        if tempPoniedzialek == pogodaPopojutrze:
            print("\nW poniedzialek temperatura zgadza się")
            print(".............................")
        else:
            print("\nW poniedzialek temperatura NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        #Ikona z kwadratu w poniedzialek
        ikonaPoniedzialek = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[2]/div[3]/img").get_attribute("title")
        print(ikonaPoniedzialek.lower())

        #Ikona z mapy w poniedzialek
        naStroniePoniedzialekIkona = driver.find_element_by_xpath("//a[@id='"+naMapie+"']/img").get_attribute("title")
        print(naStroniePoniedzialekIkona)

        if ikonaPoniedzialek.lower() == naStroniePoniedzialekIkona:
            print("\nW poniedzialek pogoda zgadza się")
            print(".............................")
        else:
            print("\nW poniedzialek pogoda NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        ###########################################################################################
        #kliknij dzisiaj na mapie
        MapaDzisiaj = driver.find_element_by_xpath(".//*[@id='box-map-default']/div/div[2]/div[1]/ul/li[1]/a").click()
        time.sleep(1)

        #temp na mapie dzisiaj
        tempNaStronieDzis = driver.find_element_by_id(naMapie)
        pogodaDzis = tempNaStronieDzis.text
        print(pogodaDzis)

        #Temp. w kwadracie dzisiaj
        TempDzis = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[1]/div/p[2]/span").text + " " + driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[1]/div/p[2]/sup").text + "\n" + bok
        print(TempDzis)

        if TempDzis == pogodaDzis:
            print("\nDzis temperatura zgadza się")
            print(".............................")
        else:
            print("\nDzis temperatura NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return

        #Ikona z kwadratu dzisiaj
        ikonaDzis = driver.find_element_by_xpath(".//*[@id='box-info-tab3']/div[1]/img").get_attribute("title")
        print(ikonaDzis.lower())

        #Ikona z mapy dzisiaj
        naStronieDzisIkona = driver.find_element_by_xpath("//a[@id='"+naMapie+"']/img").get_attribute("title")
        print(naStronieDzisIkona)

        if ikonaDzis.lower() == naStronieDzisIkona:
            print("\nDzisiaj pogoda zgadza się")
            print(".............................")
        else:
            print("\nDzisiaj pogoda NIE ZGADZA SIE")
            print(".............................")
            driver.get_screenshot_as_file('errorTwojaPogoda.png')
            print ("Screenshoot saved")
            return


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
