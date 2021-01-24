import convert_split
from PIL import Image, ImageStat
import os
import matplotlib.pyplot as plt

bVal= {}

convert_split.split()


#calulate Image Brightness
directory = r'C:\Users\varun\Desktop\plateReader\savedIMG'
for fileNum,filename in enumerate(os.listdir(directory)):
    img = Image.open(os.path.join(directory, filename))
    stat = ImageStat.Stat(img)
    bVal[f'Img{fileNum+1}'] = stat.mean[0]



#plot on histogram

plt.bar(range(len(bVal)), list(bVal.values()), align='center',width = 0.5, color='#0504aa',alpha=0.7)
plt.xticks(range(len(bVal)), list(bVal.keys()))
plt.xlabel('split images')
plt.ylabel('brightness')
plt.title('Brightness at diffrent points of diffusor',fontsize=15)
plt.show()






