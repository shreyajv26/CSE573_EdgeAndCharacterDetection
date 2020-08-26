"""
Character Detection

The goal of this task is to experiment with template matching techniques. Specifically, the task is to find ALL of
the coordinates where a specific character appears using template matching.

There are 3 sub tasks:
1. Detect character 'a'.
2. Detect character 'b'.
3. Detect character 'c'.

You need to customize your own templates. The templates containing character 'a', 'b' and 'c' should be named as
'a.jpg', 'b.jpg', 'c.jpg' and stored in './data/' folder.

Please complete all the functions that are labelled with '# TODO'. Whem implementing the functions,
comment the lines 'raise NotImplementedError' instead of deleting them. The functions defined in utils.py
and the functions you implement in task1.py are of great help.

Do NOT modify the code provided.
Do NOT use any API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import any library (function, module, etc.).
"""

import matplotlib.pyplot as plt
import argparse
import json
import os

import utils
from task1 import *   # you could modify this line


def parse_args():
    parser = argparse.ArgumentParser(description="cse 473/573 project 1.")
    parser.add_argument(
        "--img_path", type=str, default="./data/proj1-task2-png.png",
        help="path to the image used for character detection (do not change this arg)")
    parser.add_argument(
        "--template_path", type=str, default="./data/c.png",
        choices=["./data/a.jpg", "./data/b.jpg", "./data/c.jpg"],
        help="path to the template image")
    parser.add_argument(
        "--result_saving_directory", dest="rs_directory", type=str, default="./results/",
        help="directory to which results are saved (do not change this arg)")
    args = parser.parse_args()
    return args

#Yoo, Jae Chern & Han, Tae. (2009). Fast Normalized Cross-Correlation. Circuits, Systems and Signal Processing. 28. 819-843. 10.1007/s00034-009-9130-7. 

'''
TY  - JOUR
AU  - Khalil, M
AU  - Ibrahim, Ahmed
PY  - 2015/01/10
SP  - 1
EP  - 9
T1  - Quick Techniques for Template Matching by Normalized Cross-Correlation Method
VL  - 11
DO  - 10.9734/BJMCS/2015/16461
JO  - British Journal of Mathematics & Computer Science
ER  - 

'''

def norm_cross_correlation(img,template):
    
        row_image = len(img)
        col_image = len(img[0])
        #print(row_image,col_image)
    
        row_template = len(template)
        col_template = len(template[0])
        #print(row_template,col_template)
        
        #Get the center element of the temnplate and pad the image with those many layers
        pad_row = row_template//2
        pad_col = col_template//2
        
        #img_ncc = []
        img_ncc = utils.zero_pad(img,pad_row,pad_col)
        
        row_image_pad = len(img_ncc)
        col_image_pad = len(img_ncc[0])
        
        #img_ncc = [[0 for r in range(row_image_pad)] for s in range(col_image_pad)]
        
        for i in range(row_image_pad-row_template+1):
            for j in range(col_image_pad-col_template+1):
                
                cropped_img = utils.crop(img_ncc,i,i+row_template,j,j+col_template)
                product = utils.elementwise_mul(cropped_img,template)
                
                
                #squaring cropped image
                cropped_sqr_img = utils.elementwise_mul(cropped_img,cropped_img)
                
                #squaring template
                sqr_template = utils.elementwise_mul(template,template)
                
                sum1 = 0
                sum_cropped_sqr_img = 0
                sum_sqr_template = 0
                
                for x in range(len(product)):
                    for y in range(len(product[x])):
                        #summation of cropped image and template
                        sum1 += product[x][y]
                        
                        
                        #summation of square of cropped image
                        sum_cropped_sqr_img += cropped_sqr_img[x][y]
                        
                        
                        #summation of square of template
                        sum_sqr_template += sqr_template[x][y]
                        
                        
                img_ncc[i][j] = sum1/((sum_cropped_sqr_img * sum_sqr_template)**0.5)
        
        return img_ncc


        
def detect(img, template):
    """Detect a given character, i.e., the character in the template image.

    Args:
        img: nested list (int), image that contains character to be detected.
        template: nested list (int), template image.

    Returns:
        coordinates: list (tuple), a list whose elements are coordinates where the character appears.
            format of the tuple: (x (int), y (int)), x and y are integers.
            x: row that the character appears (starts from 0).
            y: column that the character appears (starts from 0).
    """
    # TODO: implement this function.
    #raise NotImplementedError
    #https://www.mvtec.com/doc/halcon/12/en/find_ncc_model.html
    
    image_det = norm_cross_correlation(img,template)
    
    row_image = len(image_det)
    col_image = len(image_det[0])
    #print(row_image,col_image)
    
    row_template = len(template)
    col_template = len(template[0])
    #print(row_template,col_template)
    
    
    coordinates = []
    threshold = 0.7
    
    for i in range (row_image):
        for j in range (col_image):
            if image_det[i][j] > threshold:
                coordinate = [i,j]
                coordinates.append(coordinate)
    
    #print(coordinates)
    return coordinates



def save_results(coordinates, template, template_name, rs_directory):
    results = {}
    results["coordinates"] = sorted(coordinates, key=lambda x: x[0])
    results["templat_size"] = (len(template), len(template[0]))
    with open(os.path.join(rs_directory, template_name), "w") as file:
        json.dump(results, file)


def main():
    args = parse_args()

        
    img = read_image(args.img_path)
    #img = read_image("C:\\Shreya\\proj1-task2-png.png")
    
    template = read_image(args.template_path)
    #template = read_image("C:\\Shreya\\a.png")
    
    coordinates = detect(img, template)

    template_name = "{}.json".format(os.path.splitext(os.path.split(args.template_path)[1])[0])
    save_results(coordinates, template, template_name, args.rs_directory)
    #norm_cross_correlation(img,template)

    
    #from matplotlib.patches import Arrow, Circle
    #img = cv2.imread("C:\\Shreya\\proj1-task2-png.png")
    #fig, ax = plt.subplots(1)
    #ax.imshow(img)
    #for i in coordinates:
     #   ax.add_patch(Circle((i[1], i[0]), radius=1, color='red'))
    #plt.show(fig)

    
if __name__ == "__main__":
    main()
