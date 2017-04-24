import os
import csv
import re
from guessit import guessit

raw_names = []

find_ill = re.compile('(.csv|py)')

for x in os.listdir():
    raw_names.append(str(x))

clean_names = dict()

for name in raw_names:
    if find_ill.search(name) == None:
        clean_names[guessit(name).get('title')] = str(guessit(name).get('year'))

with open('updated_list.csv', 'w') as delete_it:
    add_top = csv.writer(delete_it)
    add_top.writerow(["Name","Year"])

for k,v in clean_names.items():
    flag = 0
    with open('current_movies.csv', 'r') as curr:
        r = csv.reader(curr)
        for row in r:
            if row[0] == k:
                flag = 1
        if flag == 0:
            with open('current_movies.csv', 'a') as update_curr:
                w = csv.writer(update_curr)
                w.writerow([k,v])
            with open('updated_list.csv', 'a') as new_list:
                u = csv.writer(new_list)
                u.writerow([k,v])
            print(k + " " + v + " has been added to the list!")
