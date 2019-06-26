import json
import requests
import pandas as pd


with open (".gitignore", "r") as miarchivo:
    acceso = miarchivo.readlines()

repo = 'ironhack-datalabs/madrid-oct-2018'
get_forks = 'http://api.github.com/repos/'+ repo +'/forks'

res_fork = requests.get(get_forks, auth=('Jjespper', acceso))

results_fork = res_fork.json()

languages = set()

for i in range(len(results_fork)):
    languages.add(results_fork[i]['language'])

print(languages)