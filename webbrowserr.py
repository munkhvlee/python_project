import webbrowser

text = input("input: ")
url = "https://translate.google.com/#en/mn/" + text
#https://translate.google.com/

webbrowser.open(url)
