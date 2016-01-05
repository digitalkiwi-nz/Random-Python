# ChromePass.py:	Decrypt passwords stored by Chrome in "login Data" file
# Author:    		David White
# Date:      		October 2015

from os import getenv
import sqlite3
import win32crypt

# Connect to the database file
try:
    con = sqlite3.connect(getenv('APPDATA') + '\..\Local\Google\Chrome\User Data\Default\Login Data')
except Exception as e:
    print e

# Get the data
curs = con.cursor()
curs.execute('SELECT action_url, username_value, password_value FROM logins')
for result in curs.fetchall(): # Decrypt the Password
	site_name = result[0]
	user_id = result[1]
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		print 'Site: ' + site_name
		print 'Username: ' + user_id
		print 'Password: ' + password + '\n'