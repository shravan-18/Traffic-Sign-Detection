from PIL import Image
import os

image_dir = r"D:\\PJT\\PJT-Datasets\\Chinese-Traffic-Signs"
image_classes = []

for image in os.listdir(image_dir):
    if image.split('_')[0] not in image_classes:
        image_classes.append(image.split('_')[0])

for Class in image_classes:
    os.makedirs(os.path.join(image_dir, Class), exist_ok=True)

for image in os.listdir(image_dir):
    if image.endswith('.png'):
        curr_img_path = os.path.join(image_dir, image)
        image_folder_path = os.path.join(image_dir, image.split('_')[0], image)

        os.rename(curr_img_path, image_folder_path)



print("Images moved to specific Class folders!")