import os

def count_images(dir):

  count = 0

  for file in os.listdir(dir):

    count += 1

  return count

dir = 'cell_images/train/parasitized'

print(count_images(dir))