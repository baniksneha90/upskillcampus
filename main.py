print("WElcome to Smart URL Shortener")

from utils import gen_shortcode
from database import save_url
long_url=input("enter the url:")
short_code=gen_shortcode()
save_url(long_url, short_code)

print("original url :", long_url)
print("short_code:", short_code)

print("Saved Successfully!")