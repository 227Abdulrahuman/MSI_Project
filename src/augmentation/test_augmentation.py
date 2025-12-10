import cv2
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

def testFlipAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_flip.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.flip(image)
    cv2.imwrite(str(output_path / "modified_flip.jpg"), modified_image)
testFlipAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")

def testRotateAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_rotate.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.rotate(image)
    cv2.imwrite(str(output_path / "modified_rotate.jpg"), modified_image)
testRotateAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")


def testGaussianNoiseAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_gaussian_noise.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.gaussian_noise(image)
    cv2.imwrite(str(output_path / "modified_gaussian_noise.jpg"), modified_image)
testGaussianNoiseAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")

def testSaltAndPepperNoiseAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_salt_and_pepper_noise.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.salt_and_pepper_noise(image)
    cv2.imwrite(str(output_path / "modified_salt_and_pepper_noise.jpg"), modified_image)
testSaltAndPepperNoiseAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")

def testCombinedAugmentation(image_name):
    image_path = working_dir / "../../data/raw" / image_name
    output_path = working_dir / "../../data/tests"

    image = cv2.imread(str(image_path))
    cv2.imwrite(str(output_path / "original_combined.jpg"), image)


    augmentor = Augmentor()
    modified_image = augmentor.augment(image)
    cv2.imwrite(str(output_path / "modified_combined.jpg"), modified_image[1])
testCombinedAugmentation("glass/38d5d187-6719-43bd-a0ca-fb6718d673ef.jpg")
