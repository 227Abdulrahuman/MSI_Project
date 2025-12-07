import cv2, numpy as np, random

class Augmentor:
    def __init__(self):
        self.techniques = [
            self.flip,self.change_brightness# self.rotate, , self.add_noise
        ]

    def flip(self, img):
        return cv2.flip(img, 1)

    def change_brightness(self, img):
        hsb = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsb = np.array(hsb, dtype=np.float64)

        brightness_ration = random.uniform(0.5, 1.4)
        hsb[:, :, 2] = hsb[:, :, 2] * brightness_ration
        hsb[:,:,2] = np.clip(hsb[:,:,2], 0, 255)

        hsb = np.array(hsb, dtype=np.uint8)
        rgb = cv2.cvtColor(hsb, cv2.COLOR_HSV2BGR)
        return rgb

    def generateSample(self, img):
        return self.filp(img)