import urllib.request
with urllib.request.urlopen('https://www.gutenberg.org/files/1342/1342-0.txt') as response:
    html = response.read().decode('utf-8')

print(html)