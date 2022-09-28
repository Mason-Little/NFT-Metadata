import json
import os
import cv2 as cv

file_names = os.listdir('Input')
file_names = [i.split(".")[0] for i in file_names]
print(file_names)

Main_Image_dir = 'Data_Upload\\images'
Main_Json_dir = 'Data_Upload\\json'
image_path = ['input\\' + i + '.jpg' for i in file_names]

all_images = []
for image in image_path:
    image = cv.imread(image)
    all_images.append(image)

image_len = len(all_images)

json_data = {"Pose": input("Pose: "), "background": input("Background: "), "Hat": input("Hat: "),
             "Head_Backwords": input("Head_Backwords: "), "Putin": input("Putin: ")}

file_name = json_data["Pose"] + ',' + json_data["background"] + ',' + json_data["Hat"] + ',' + json_data[
    "Head_Backwords"] + ',' + json_data["Putin"]
try:
    if not os.path.exists(os.path.join(Main_Json_dir, file_name)):
        os.makedirs(f"{os.path.join(Main_Image_dir, file_name)}_0")

    if not os.path.exists(os.path.join(Main_Image_dir, file_name)):
        os.makedirs(f"{os.path.join(Main_Json_dir, file_name)}_1")
except FileExistsError:
    pass

for file in file_names:
    with open(f"{os.path.join(Main_Json_dir, file_name)}_1\\{file}.json", 'w') as f:
        json.dump(json_data, f)

for i in range(image_len):
    cv.imwrite(f"{os.path.join(Main_Image_dir, file_name)}_0\\{file_names[i]}.jpg", all_images[i])