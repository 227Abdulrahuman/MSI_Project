import cv2
from augmentation import Augmentor

def testFilpAugmentation():
    file_path = '/home/hacker/PycharmProjects/MSI_Project/data/raw/glass/0aa1cd06-402d-408b-804e-e927d14a3972.jpg'
    output_dir = '/home/hacker/PycharmProjects/MSI_Project/data/tests'
    img = cv2.imread(file_path)
    cv2.imwrite(f"{output_dir}/0_original.jpg", img)

    augmentor = Augmentor()
    fliped_image = augmentor.flip(img)
    cv2.imwrite(f"{output_dir}/0_flipped.jpg", fliped_image)

testFilpAugmentation()