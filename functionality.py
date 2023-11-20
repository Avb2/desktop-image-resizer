from cvFunc import MyCv

class ButtonFunctionality:
    @staticmethod
    def create_size_tuple(xVal, yVal):
        return (int(xVal), int(yVal))

    @staticmethod
    def enter_btn_functionality(sizeTuple, imagePath, resizedImagePath):
        image = MyCv(imagePath)

        image.resize_image(sizeTuple, resizedImagePath)