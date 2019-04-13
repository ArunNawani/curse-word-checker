Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
def read_text():
    quotes = open()         #drop the text file location in paranthesis you want to check
    content = quotes.read()
    print(content)
    quotes.close()
    check(content)


def check(text_to_read):
    checker = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_read)
    output = checker.read()
    print(output)
    checker.close()

read_text()
