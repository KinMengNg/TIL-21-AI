#to change the name of files in noisy which have the same bloody name as the not noisy for some reason
import os
target = 'D:/TIL21/Hackathon/augmented_dataset_verynoisy'
counter = 0
for label in os.listdir(target):
  for filename in os.listdir(f'{target}/{label}'):
      os.rename(f'{target}/{label}/{filename}', f'{target}/{label}/{filename[:-4]}_NOISY.wav')
      counter += 1
      if counter % 20 == 0:
          print('Done with:', counter)
      #testing if it works
      #print(filename)
      #print(f'{target}/{label}/{filename[:-4]}_NOISY.wav')
