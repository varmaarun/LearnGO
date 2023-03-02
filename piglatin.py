from operator import truediv
from urllib.request import ProxyDigestAuthHandler


def pig_it(text):
    pl=""
    end=True

    for word in text.split():
        if word.isalnum():
            pl=pl+word[1:]+word[:1]+"ay" +" "
            end=True
            
        else:
            pl=pl+word
            end=False

    if end:
        pl=pl[:-1]
    return pl

print(pig_it("Pig latin is cool"))