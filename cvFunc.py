import cv2
import os

class MyCv:
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.imageObj = cv2.imread(self.imagePath)
        self.imageSize = self.imageObj.shape

    def resize_image(self, newSizeTuple, resizedImagePath):
        resizedImage = cv2.resize(self.imageObj, (newSizeTuple), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(resizedImagePath, resizedImage)
