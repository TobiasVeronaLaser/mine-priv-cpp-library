import os
import shutil
import time
import imagehash
from PIL import Image # pip install Pillow==9.5.0

root = '.\\..\\..'

number_length = 9

def is_valid_image_pillow(file_name):
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False

def is_same_image(image_path_0, image_path_1):
    input_image_0 = Image.open(image_path_0)
    input_image_1 = Image.open(image_path_1)

    width_0, height_0 = input_image_0.size
    width_1, height_1 = input_image_1.size

    if width_0 != width_1 or height_0 != height_1:
        return False
    for w in range(width_0):
        for h in range(height_0):
            #print(str(input_image_0.getpixel((w, h))) + "\t" + str(input_image_1.getpixel((w, h))) )
            
            if input_image_0.getpixel((w, h)) != input_image_1.getpixel((w, h)):
                return False
    return True

def get_files(filepath: str):
    files = []
    folders = []
    for f in os.listdir(filepath):
        temp_filepath = filepath + "\\" + f
        if os.path.isfile(temp_filepath):
            if not is_valid_image_pillow(temp_filepath):
                continue
            if 0 == len(os.path.splitext(temp_filepath)[-1].lower()):
                continue
            # print("file: " + f)
            files.append(temp_filepath)
        if os.path.isdir(temp_filepath):
            #print("folder: " + f)
            folders.append(f)
    for f in folders:
        sub_files = get_files(filepath + "\\" + f )
        files += sub_files
    return files

def filter_doubles(input_folder, output_folder):
    start_time = time.time()
    print("Collect filepaths.")
    input_files = get_files(input_folder)
    print("Done collecting.")
    print("Time collecting: " + str(time.time() - start_time))
    output_files = []
    current_input_counter = 0
    output_file_counter = 0
    print("Filtering")
    start_time = time.time()
    for input_file in input_files:
        current_input_counter += 1
        to_copy = True
        for output_file in output_files:
            #print(str(input_file) + "\t" + str(output_folder + "\n" + output_file))
            if is_same_image(input_file, output_folder + "\\" + output_file):
                to_copy = False
                break
        if to_copy:
            output_file_counter += 1
            print(str(output_file_counter) + "|" + str(current_input_counter) + "|" + str(len(input_files))+ "\t" + input_file)
            temp = "image-" + str(output_file_counter).zfill(number_length) + "." +  input_file.split('.')[-1]
            shutil.copyfile(input_file, output_folder + "\\" + temp)
            output_files.append(temp)
    print("Done Filtering")
    print("Time filtering: "  + str(time.time() - start_time))
    print("Counted " + str(len(input_files)) + " original files.\nCopied " + str(output_file_counter) + " files.")

def filter_doubles_hash(input_folder, output_folder):
    start_time = time.time()
    print("Collect filepaths.")
    input_files = get_files(input_folder)
    print("Done collecting.")
    print("Time collecting: " + str(time.time() - start_time))
    output_hashes = []
    current_input_counter = 0
    output_file_counter = 0
    print("Filtering")
    start_time = time.time()
    for input_file in input_files:
        current_input_counter += 1
        to_copy = True
        image_hash = imagehash.average_hash(Image.open(input_file))
        if image_hash in output_hashes:
            to_copy = False                
        if to_copy:
            output_file_counter += 1
            print(str(output_file_counter) + "|" + str(current_input_counter) + "|" + str(len(input_files))+ "\t" + input_file)
            temp = output_folder + "\\"  + "image-" + str(output_file_counter).zfill(number_length) + "." +  input_file.split('.')[-1]
            shutil.copyfile(input_file, temp)
            output_hashes.append(imagehash.average_hash(Image.open(temp)))
    print("Done Filtering")
    print("Time filtering: "  + str(time.time() - start_time))
    print("Counted " + str(len(input_files)) + " original files.\nCopied " + str(output_file_counter) + " files.")

def test_get_files():
    data = get_files(root + "\\static\\images\\test")
    print(data)

def test_compare_files():
    files = get_files(root + "\\static\\images\\test")
    print(is_same_image(files[0], files[0]))
    print(is_same_image(files[0], files[1]))

def test_filter_files():
    filter_doubles(root + "\\static\\images\\test", root + "\\static\\images\\test_output")

if __name__ == "__main__": 
    #filter_doubles("F:\\sorted", "F:\\filtered")
    #filter_doubles("C:\\Users\\TobiasLaser\\mine-priv-cpp-library\\static\\images\\test","C:\\Users\\TobiasLaser\\mine-priv-cpp-library\\static\\images\\test_output")
    #filter_doubles_hash("C:\\Users\\TobiasLaser\\mine-priv-cpp-library\\static\\images\\test","C:\\Users\\TobiasLaser\\mine-priv-cpp-library\\static\\images\\test_output")
    #print(is_same_image("C:\\Users\\TobiasLaser\mine-priv-cpp-library\\static\\images\\test\\IMG_20230701_143042-2.jpg", "C:\\Users\\TobiasLaser\mine-priv-cpp-library\\static\\images\\test\\IMG_20230701_143042.jpg"))
    #filter_doubles(root + "\\static\\images\\2023", root + "\\static\\images\\filter_output")
    filter_doubles_hash(root + "\\static\\images\\2023", root + "\\static\\images\\filter_output")
    # test_get_files()