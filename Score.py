from Utils import *
from os import path

def add_score(points):

    if path.isfile(SCORES_FILE_NAME):
     f = open(SCORES_FILE_NAME, 'r+')
     s = f.readline()
     updated_score = int(s) + points
     f.seek(0)
     f.write(str(updated_score))
    else:
     f = open(SCORES_FILE_NAME, 'w+')
     f.write(str(points))

    f.close()




