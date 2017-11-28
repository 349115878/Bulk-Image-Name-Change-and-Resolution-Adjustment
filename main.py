import os
from PIL import Image


def scale_down_image(path):
    for file_name in os.listdir(path):
        if os.path.splitext(path + file_name)[1] == ".jpg":
            im = Image.open(path + file_name)
            print(file_name)
            width, height = im.size
            if width > height:
                size = (1920, 1080)
            else:
                size = (1080, 1920)
            im.thumbnail(size)
            im.save(path + "complete/" + file_name)
            im.close()


def change_name(path):
    num = 0
    for file_name in os.listdir(path):
        if os.path.splitext(path + file_name)[1] == ".jpg":
            os.rename(path + file_name, path + str(num) + ".jpg")
            num = num + 1


def main():
    path = "/Users/nnelson/Downloads/Colorful_720p/"
    print("Here is the path: ", path)
    print("Running Change Name")
    change_name(path)
    print("Finished Running Change Name.\nRunning Scale Down Image now.")
    scale_down_image(path)
    print("PROGRAM FINISHED")


main()
