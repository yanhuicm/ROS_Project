import numpy as np
import cv2
import os

cwd = os.getcwd()

def convert(file):
    cv2_img = np.genfromtxt((cwd + '/timed/' + file), delimiter=',')
    cv2.imwrite((cwd + '/timed/images/' + file[:-4] + '.jpeg'), cv2_img)

def main(args=None):
    if os.path.exists(cwd + '/timed/images') == False:
        os.mkdir(cwd + '/timed/images')
    for file in os.listdir(cwd + '/timed'):
        if file[-4:] == '.csv':
            convert(file)
    print('Conversion complete.')
