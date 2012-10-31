#/bin/env/python

#
# Copyright 2012 Kurtis L. Nusbaum
#
# This file is part of derpoker.
#
# derpoker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# derpoker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with derpoker.  If not, see <http://www.gnu.org/licenses/>.
#
from facebook import FBPASS, FBLOGIN, SQL_CONNECT_STRING
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from pyvirtualdisplay import Display
import sqlalchemy


def openLogConnection():
  engine = sqlalchemy.create_engine(SQL_CONNECT_STRING)
  conn =engine.connect()
  return  conn

def closeLogConnection(conn):
  conn.close()

def logPoke(logConn, poker, pokerlink):
  try:
    logConn.execute("INSERT INTO pokeviewer_poke(poker, poke_time, poker_profile_link) VALUES ('{0}', now(), '{1}')".format(poker,pokerlink))
  except Exception as f:
    print str(f)

def doLogin(browser):
  email = browser.find_element_by_id('email')
  email.send_keys(FBLOGIN)

  password = browser.find_element_by_id('pass')
  password.send_keys(FBPASS)

  browser.find_element_by_id('loginbutton').click()

def loopThatShit(browser, logConn):
  print "Getting facebook.com/pokes"
  browser.get("http://www.facebook.com/pokes")
  print "Starting poke loop"
  i = 0
  while(True):
      if i>360:
        i=0
        browser.get("http://www.facebook.com/pokes")
      else:
        i += 100

      pokeDashboard = browser.find_element_by_class_name('pokesDashboard')
      pokers = pokeDashboard.find_elements_by_class_name('objectListItem')
      for poker in pokers:
        try:
          pokeLink = poker.find_element_by_link_text('Poke Back')
          pokeheader = poker.find_element_by_class_name('pokeHeader')
          pokername = pokeheader.text.rsplit(' ',3)[0]
          pokerlink = pokeheader.find_element_by_partial_link_text(pokername).get_attribute('href').split('/')[-1]
          pokeLink.click()
          logPoke(logConn, pokername, pokerlink)
        except NoSuchElementException:
          pass

      sleep(1)

print "Opening display"
display = Display(visible=0, size=(800, 600))
display.start()

print "Starting Firefox"
browser = webdriver.Firefox() # Get local session of firefox
print "Getting facebook.com"
browser.get("http://www.facebook.com") # Load page
print "loggin in..."
doLogin(browser)
print "logged in mofo"
print "opening database logging connection"
conn = openLogConnection()
print "db connection open"

if conn == None:
  print "Connection is none"
  exit(1)
try:
  loopThatShit(browser, conn)
except Exception as f:
  print "Error: " + str(f)
finally:
  closeLogConnection(conn)

