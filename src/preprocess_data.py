import data_manager
import augmentation.augmentation as augmentation

proccess = data_manager.DataManager()
augment = augmentation.Augmentor()

data = proccess.load_data()
proccessed_data = {}
for category, images in data.items():
    proccessed_data[category] = []
    for img in images:
        aug_img_info = augment.augment(img)
        if aug_img_info[0]:
            proccessed_data[category].append(aug_img_info[1])
            print(f"Augmented image for category '{category}'")
proccess.save_data(proccessed_data)