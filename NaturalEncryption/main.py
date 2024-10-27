import requests as req
import random as rand
import re

GLOBAL_aCode = rand.randint(10000, 99999)


def temperature():
  url = f'https://wttr.in/{GLOBAL_aCode}?format=%t'
  r = req.get(url)
  tempreq = r.text
  resultStr = re.sub('[^0-9]', '', tempreq)
  resultInt = int(resultStr) + 273
  return resultInt


base = temperature()
print(base)


def numGen(base, filename):
  text = open(f'{filename}.txt', 'r')
  textLst = [words for words in text]
  print(textLst)


numGen(base)
