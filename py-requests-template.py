import requests
requests.packages.urllib3.disable_warnings()

beg_no = 1800
end_no = 3800

SESSION = 'session_value'
VERBOSE = False

def py_req(target_param):
    url = "https://example.com"
    cookies = {"SESSION": SESSION}
    headers = {"Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Content-Type": "application/json", "waitForResponse": "true", "Connection": "close"}
    body_data = {"json_parent":{"json_child_1":target_param,"json_child_2":"child_value_2"}}
    return requests.post(url, headers=headers, cookies=cookies, json=body_data, verify=False).json()

print("Python Requests template running:")

for i in range(beg_no, end_no):
    data = py_req(i)
    target = "target_string"
    error = "error_string"
    if error in data:
        if VERBOSE:
            print("[-] ID not found: {}".format(i))
    elif target in data:
        print("[+] Target found: {}".format(data['json_parent']['json_child_1']))
    else:
        if VERBOSE:
            print("[*] Unexpected error occurred while checking ID: {}".format(i))
