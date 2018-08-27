from label_image2 import label_image

import cv2

from glob import glob

image_files = glob('/home/crupanshu/AnacondaProjects/tensorflow-for-poets-2/test_data/*.*')

for image_file in image_files:
  image = cv2.imread(image_file)
  print(image_file, " -> ", label_image(image))
