"""
Implementation of Binary and Multiclass Dice Coefficients. Copied from stackoverflow.


# Full credit to:
# https://stackoverflow.com/questions/61488732/how-calculate-the-dice-coefficient-for-multi-class-segmentation-task-using-pytho
"""

import numpy as np
import matplotlib.pyplot as plt


def dice_coef(y_true, y_pred):
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    smooth = 0.0001
    return (2. * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth)

def dice_coef_multilabel(y_true, y_pred, numLabels):
    dice_coefs = np.zeros(numLabels)
    
    for index in range(numLabels):
        dice_coefs[index] = dice_coef(y_true[:,:,:,index], y_pred[:,:,:,index])
    return dice_coefs # taking average


if __name__ == "__main__":
    num_class = 3

    imgA = np.random.randint(low=0, high= 2, size=(5, 64, 64, num_class) ) # 5 images in batch, 64 by 64, num_classes map
    imgB = np.random.randint(low=0, high= 2, size=(5, 64, 64, num_class) )


    plt.imshow(imgA[0,:,:,0]) # for 0th image, class 0 map
    plt.show()

    plt.imshow(imgB[0,:,:,0]) # for 0th image, class 0 map
    plt.show()

    dice_score = dice_coef_multilabel(imgA, imgB, num_class)
    print(f'For A and B {dice_score}')

    dice_score = dice_coef_multilabel(imgA, imgA, num_class)
    print(f'For A and A {dice_score}')