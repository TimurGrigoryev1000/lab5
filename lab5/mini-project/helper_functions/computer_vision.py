from PIL import Image
import numpy as np


# Takes in image1 and image2 locations and t1
# returns a Boolean indicating if a "person" is in the image based on t1
def person_detected(image1_file, image2_file, t1):

    # load images and convert to grayscale
    img1 = Image.open(image1_file).convert("L")
    img2 = Image.open(image2_file).convert("L")

    # convert images to matrices
    mat1 = np.array(img1, dtype=np.int32)
    mat2 = np.array(img2, dtype=np.int32)

    # background subtraction
    diff = mat2 - mat1

    # sum of absolute differences
    diff_score = np.sum(np.abs(diff))

    # compare to threshold
    if diff_score > t1:
        return True
    else:
        return False
