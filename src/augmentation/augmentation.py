import cv2, numpy as np, random, glob
from pathlib import Path

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


    def augment_all(self):
        working_dir = Path(__file__).parent

        categories = {
            'glass': glob.glob(str(working_dir / '../../data/raw/glass' / '*.jpg')),
            'metal': glob.glob(str(working_dir / '../../data/raw/metal' / '*.jpg')),
            'paper': glob.glob(str(working_dir / '../../data/raw/paper' / '*.jpg')),
            'cardboard': glob.glob(str(working_dir / '../../data/raw/cardboard' / '*.jpg')),
            'plastic' : glob.glob(str(working_dir / '../../data/raw/plastic' / '*.jpg')),
            'trash' : glob.glob(str(working_dir / '../../data/raw/trash' / '*.jpg')),
        }

        for category, paths in categories.items():
            for file_path in paths:
                img = cv2.imread(file_path)
                if img is None: continue

                img = self.flip(img)

                output_name = Path(file_path).name
                output_path = working_dir / f'../../data/processed/{category}' / output_name

                Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                cv2.imwrite(str(output_path), img)



augmentor = Augmentor()
augmentor.augment_all()
