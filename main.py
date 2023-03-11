import requests
 
r = requests.get('https://www.google.com/search?q=gugu+gaga&oq=gugu+gaga&aqs=chrome.0.0i355i512j46i512j0i512l2j0i22i30l6.3632j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:39af2ad0,vid:OJkSCvz0RgM')
print(r)

class Browser:
  name = "name"
  age = 24

  def __init__(self, url):
    self.url = url
    

def load_page(self):
  r = requests.get(self.url)
  if r.status_code == 200:
    print ("Page is loaded")
  else:
    print("some error....")




my_b = Browser("https://www.google.com")
my_b.load_page()
