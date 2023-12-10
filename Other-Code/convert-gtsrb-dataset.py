from PIL import Image
import os

def convert_ppm_to_jpg(input_path, output_path):
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")

images_dir = r"D:\\PJT\\Pjt-Datasets\\GTSRB"
class_names = os.listdir(images_dir)

for Class in class_names:
    class_dir = os.path.join(images_dir, Class)
    Class_items = os.listdir(class_dir)

    for file in Class_items:
        filepath = os.path.join(class_dir, file)
        if file.endswith(".ppm"):
            output_filename = file.split('.')[0] + ".jpg"
            output_path = os.path.join(class_dir, output_filename)
            convert_ppm_to_jpg(filepath, output_path)

        else:
            os.remove(filepath)

    print("Class: ", Class, " - done!")


print("Images converted to .jpg files")