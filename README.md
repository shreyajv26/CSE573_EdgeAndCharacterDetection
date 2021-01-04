# CSE573_EdgeAndCharacterDetection
CSE 573 - Computer Vision and Image Processing


1. Edge Detection [35 points]
The goal of this task is to experiment with two commonly used edge detection operator, i.e., Prewitt operator and Sobel operator, and familiarize you with tricks, e.g., padding, commonly used by computer vision practitioners. Specifically, the task is to detect edges in a given image, which is named “proj1-task1.jpg” and is stored in “./data/”.
You are required to implement all the functions that are labelled with “# TODO” in “task1.py” and “utils.py”. In “task1.py” and “utils.py”, we not only provide hints to you, but also provide utility functions that could be used as building blocks for you to complete this task. Therefore, you only need to write about 40 lines of code. Your code should be able to generate images that are identical to those stored in “./results/” (Note that images in “./results/” are provide to you for reference only. At test time, a different image will be used as input and the correct output images will be different from those already stored in “./results/”).
Comment the lines “raise NotImplementedError” instead of deleting them, when you implement the functions labelled with “# TODO”.

2. Character Detection [65 points]
The goal of this task is to experiment with template matching algorithms. Specifically, the task is to find a specific character (or set of characters) in a given image, which is named “proj1-task2.pgm” and is store the results in “./data/”. You are required to implement a function named “detect” in “task2.py”, which detects a character in an image. The function “detect” takes a given image and a given template (that you will implement) that contains a character as input and returns the coordinates (i.e., coordinates of the top-left pixel) of the character contained in the template.
