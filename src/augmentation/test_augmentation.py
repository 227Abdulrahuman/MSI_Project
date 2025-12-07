import cv2
from debian.debtags import output
from augmentation import Augmentor
from pathlib import Path

working_dir = Path(__file__).parent


def testBrightnessAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_brightness.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.change_brightness(image)
    cv2.imwrite(str(output_path / "modified_brightness.jpg"), modified_image)

testBrightnessAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")
