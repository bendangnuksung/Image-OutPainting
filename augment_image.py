import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import random


brightness = iaa.Add((-7, 7), per_channel=0.5)
contrast = iaa.ContrastNormalization((0.8, 1.6), per_channel=0.5)
perspective = iaa.PerspectiveTransform(scale=(0.025, 0.090))
gaussian_noise = iaa.AdditiveGaussianNoise(loc=0, scale=(0.03*255, 0.04*255), per_channel=0.5)
crop = iaa.Crop(px=(0, 25))


def aug_image(my_image):
    image = my_image.copy()
    if random.choice([0,0,1]):
        image = perspective.augment_image(image)
    if random.choice([0,0,1]):
        image = brightness.augment_image(image)
    if random.choice([0,0,1]):
        image = contrast.augment_image(image)
    if random.choice([0,0,1]):
        image = gaussian_noise.augment_image(image)
    if random.choice([0,0,1]):
        image = crop.augment_image(image)
    return image


if __name__ == "__main__":
    import cv2
    image = cv2.imread('/home/ben/work/compare_myntra/test_image/test_images/taken_15324282418.jpg')
    aug_images = aug_image(image)
    aug_images = [aug_images]
    print(len(aug_images))
    image =  cv2.resize(image, (600,600))
    image_1 =  cv2.resize(aug_images[0], (600,600))
    cv2.imshow('1', image)
    cv2.waitKey(0)
    cv2.imshow('2', image_1)
    cv2.waitKey(0)
