import requests,time
while (True):
	time.sleep(2)
	print(requests.get("https://www.google.com"))
