#! /usr/bin/env python3
import os
import requests

path ='/data/feedback/'
files = os.listdir(path)
keys = ['title', 'name', 'date', 'feedback']
feedbacks = {}

for file in files:
  count = 0
  with open(path + file) as feedback:
      for line in feedback:
          line = line.strip()
          feedbacks[keys[count]] = line
          count +=1
  print(feedbacks)
  solicitacao = requests.post("http://34.67.61.150/feedback/", json = feedbacks)
print(solicitacao.request.body)
print(solicitacao.status_code)