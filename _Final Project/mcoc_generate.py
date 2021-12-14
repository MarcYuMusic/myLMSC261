import cv2 
import imutils
import os
import image_similarity_measures.quality_metrics
import pytesseract
import numpy as np
import sys

class Champion: 
    def __init__(self, name, node):
        self.name = name
        self.node = node

def clean_node_numbers_three(node):
    if node == "Aa":
        node = "44"
    elif node == "4&8":
        node = "38"
    elif node == "4%":
        node = "49"
    elif node == "oO":
        node = "50"
    elif node == "eB":
        node = "28"
    elif node == "on":
        node = "51"
    elif node == "a 3":
        node = "3"
    elif node == "os":
        node = "25"
    elif node == "qa":
        node = "12"
    elif node == "ag":
        node = "23"
    elif node == "og":
        node = "29"
    elif node == "oo":
        node = "22"
    return node

def clean_node_numbers_two(node):
    if node == "415":
        node = "15"
    elif node == "a5":
        node = "45"
    elif node == "of":
        node = "27"
    elif node == "S":
        node = "9"
    elif node == "413":
        node = "13"
    elif node == "AZ":
        node = "17"
    elif node == "A":
        node = "41"
    elif node == "i?":
        node = "2"
    elif node == "ao":
        node = "21"
    elif node == "A4":
        node = "44"
    elif node == "Ne":
        node = "52"
    elif node == "a1":
        node = "31"
    return node

def clean_node_numbers_one(node):
    if node == "Crs":
        node = "37"
    elif node == "cM":
        node = "20"
    elif node == "A?":
        node = "47"
    elif node == "nH?":
        node = "7"
    elif node == "1B":
        node = "8"
    elif node == "a1":
        node = "a1"
    elif node == "oa?":
        node = "27"
    elif node == "{Gg":
        node = "9"
    elif node == "49D":
        node = "13"
    elif node == "AF":
        node = "17"
    elif node == "Al":
        node = "41"
    elif node == "yo":
        node = "18"
    elif node == "EG":
        node = "6"
    elif node == "o4":
        node = "24"
    elif node == "ai":
        node = "1"
    elif node == "as":
        node = "35"
    return node

def get_number(image):
    image = imutils.resize(image, width=400)
    crop = image[140:190, 230:320]
    crop = cv2.pyrUp(crop)
    gray_image = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    placeholder, gray_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
    gray_image = cv2.pyrUp(gray_image)
    gray_image = cv2.pyrUp(gray_image)
    inverted = np.invert(gray_image)
    return pytesseract.image_to_string(inverted, config='--psm 6')

def calc_closest_val(dict, data_dir):
        result = {}
        closest = max(dict.values())
        for key, value in dict.items():
            if (value == closest):
                result[key] = closest
                image_name = key.replace(data_dir, "")
                just_name = image_name.replace(".jpg", "")   
                return just_name
        return result

def find_champ(test_img):
    values = {}
    width = int(test_img.shape[1])
    height = int(test_img.shape[0])
    dim = (width, height)
    data_dir = './champions/'
    for file in os.listdir(data_dir):
        if sys.platform.startswith('darwin'):
            if file == '.DS_Store':
                continue
        img_path = os.path.join(data_dir, file)
        data_img = cv2.imread(img_path)
        resized_img = cv2.resize(data_img, dim, interpolation = cv2.INTER_AREA)
        values[img_path] = image_similarity_measures.quality_metrics.psnr(test_img, resized_img)
    champion_name = calc_closest_val(values, data_dir)
    return champion_name
    
if __name__ == "__main__":
    faces_path = "./champions/"
    faces = os.listdir(faces_path)
    path = './screenshots/'
    screenshots = os.listdir(path)
    filename = input("Enter SQL file name:")
    f = open(filename + ".sql", "w")
    print("sqlite3 " + filename + ".db")
    f.write("sqlite3 " + filename + ".db\n")
    print("CREATE TABLE '" + filename + "' ('champ' text, 'node' integer);")
    f.write("CREATE TABLE '" + filename + "' ('champ' text, 'node' integer);\n")
    champion_collection = list()
    r = 1
    while r < 4:
        img = cv2.imread(path + screenshots[r])
        img = imutils.resize(img, width=1400)
        a = 168
        b = 268
        c = 630
        d = 730
        i = 0
        j = 0
        while i < 4:
            while j < 5:
                crop = img[a:b, c:d]
                name = find_champ(crop)
                name = name.strip()
                node = get_number(crop)
                node = node.strip()
                node = node.replace(",", "")
                node = node.replace(".", "")
                node = node.replace(")", "")
                node = node.replace("(", "")
                node = clean_node_numbers_one(node)
                node = clean_node_numbers_two(node)
                node = clean_node_numbers_three(node)
                curr = Champion(name, node)
                c += 88
                d += 88
                j += 1
                u = 0
                if (len(champion_collection) == 0):
                    champion_collection.append(curr)
                else:
                    while u < len(champion_collection):
                        if champion_collection[u].name != curr.name and champion_collection[u].node != curr.node:
                            champion_collection.append(curr)
                            break
                        u += 1
            j = 0
            a += 98
            b += 98
            c = 630
            d = 730
            i += 1
        i = 0
        j = 0
        r += 1
    while i < len(champion_collection):
        curr = champion_collection[i]
        print("INSERT INTO " + filename + " (champ, node) VALUES('" + curr.name + "', " + curr.node + ");")
        f.write("INSERT INTO " + filename + " (champ, node) VALUES('" + curr.name + "', " + curr.node + ");\n")
        i += 1