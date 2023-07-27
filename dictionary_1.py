import webbrowser

text = input("input: ")
url = "https://translate.google.co.kr/#en/mn/" + text

webbrowser.open(url)
