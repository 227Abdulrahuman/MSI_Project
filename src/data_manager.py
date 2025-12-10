import os
import pathlib as pl
import cv2

class DataManager:
    
    def load_data(self, data_dir='data/raw'):
        data_dir = pl.Path(data_dir)
        categories = [d.name for d in data_dir.iterdir() if d.is_dir()]
        print(f"Found categories: {categories}")
        data = {}
        for category in categories:
            category_path = data_dir / category
            image_files = list(category_path.glob('*.jpg'))
            print(f"Category '{category}' has {len(image_files)} images.")
            data[category] = []
            for img_file in image_files:
                img = cv2.imread(str(img_file))
                if img is None:
                    continue
                else:
                    data[category].append(img)
        return data
        
    def save_data(self, data):
        save_path = pl.Path('data/processed')
        save_path.mkdir(parents=True, exist_ok=True)
        dict_path = save_path
        for category in data.items():
            category_path = dict_path / category[0]
            category_path.mkdir(parents=True, exist_ok=True)
            for idx, img in enumerate(category[1]):
                img_filename = category_path / f"{idx}.jpg"
                cv2.imwrite(str(img_filename), img)
            print(f"Saved {len(category[1])} images to {category_path}")
    
    