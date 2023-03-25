#code for you connect the vpn or not
#import the actual scraper
import requests

url = "http://ip-api.com/json/"
key = requests.get(url)
#print(key.text)
# write name of country , state or city to check wheather your VPN is connected or not 
if "Ahemedabad" in key.text or "India" in key.text or "Gujarat" in key.text:
    print("Your VPN might not be on !!")
    safe = False
else:
    safe = True

if safe == True:
    import WebScraper
    WebScraper.Scraper()
else:
    print("IP change failed, try again later.")
