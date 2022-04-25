# !/usr/bin/python3
import os

'''
    This script was made to update URLs in a couple hundred JSON files where the JSON files 
    are organized in a hierarchy of directories.

    Biggest area for improvement is that the method used for writing files cannot edit files 
    in place, but overwrites files entirely. For this reason, the entire contents of a file
    had to be copied into memory and held in a separate variable. Then the URL updated in 
    that second copy, before overwriting the entire file with this second copy.
    
    This worked fine with smaller files, but being able to open the file for writing and 
    editing the file in place would reduce memory usage by roughly 50%.
'''

old = [
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A2-Broken_Authentication",
    "https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A6-Security_Misconfiguration",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A7-Cross-Site_Scripting_(XSS).html",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A8-Insecure_Deserialization.html",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A4-XML_External_Entities_(XXE).html",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities.html",
    "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A3-Sensitive_Data_Exposure"
]

new = [
    "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/",
    "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
    "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
    "https://owasp.org/Top10/A03_2021-Injection/",
    "https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/",
    "https://owasp.org/Top10/A03_2021-Injection/",
    "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
    "https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/",
    "https://owasp.org/Top10/A02_2021-Cryptographic_Failures/"
]


# Recurse through a file structure in the current directory.
os.chdir(".")
for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        # print(os.path.join(root, name)) 
        filename = os.path.join(root, name)

        # Open each file for reading, and store it in a variable.
        f = open(filename, "r")
        # print(f.read()) # debug
        data = f.read()

        # Check for old OWASP links and replace them.
        # Replacement is occuring in the variable in memory, not the file itself.
        for i in old:
            data = data.replace(old[i], new[i])
        f.close()

        # Open the file for writing this time, and overwrite it with the copy of
        # the file in memory that has had its links updated.
        w = open(filename, "w")
        w.write(data)
        # print(data) # debug