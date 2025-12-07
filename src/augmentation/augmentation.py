import cv2, numpy as np, random

class Augmentor:
    def __init__(self):
        self.techniques = [
            self.flip,# self.rotate, self.change_brightness, self.add_noise
        ]

    def flip(self, img):
        return cv2.flip(img, 1)

    def rotate(self, img):


    def generateSample(self, img):
        return self.filp(img)