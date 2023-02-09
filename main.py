import requests

def checkurl(url):
    url2 = f"https://www.securly.com/crextn/broker?useremail=asdfgajsdf@pausd.us&reason=crextn&host={url}&url=suicidepreventionlifeline.org&ver=1.0.0&cu=https://www.securly.com&uf=1&cf=1"
    return f"{url} allowed: {'ALLOW' in str(requests.get(url2).content)}"

print(checkurl("id.pausd.org"))

print(requests.get("https://discord.com").content)