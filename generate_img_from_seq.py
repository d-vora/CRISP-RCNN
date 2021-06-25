import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm

def custom_onehot(arr):
    img = np.zeros((len(arr),4))
    for index, value in enumerate(arr):
        if value=='-':
            pass
        elif value=='A':
            img[index][0] = 1
        elif value=='C':
            img[index][1] = 1
        elif value=='G':
            img[index][2] = 1
        elif value=='T':
            img[index][3] = 1
        else:
            img[index][0:4] = 0.25

    return img.T
  #return img

def save_img(img,loc,i):
    fig, ax = plt.subplots(figsize=(7,1))
    ax.imshow(img, interpolation='none', cmap='Blues', aspect='auto')
    plt.axis('off')
    #plt.savefig('data/'+str(loc)+'_'+str(i+1)+'.png',bbox_inches = 'tight',pad_inches=0)
    plt.savefig('moredata/'+str(loc)+'/'+str(loc)+'_'+str(i)+'.png',bbox_inches = 'tight',pad_inches=0)
    plt.close(fig)

def make_images(df):
    #start = 
    n,m = df.shape
    off_list = df['N-padded off-target'].values
    tar_list = df['N-padded target'].values
    for i in tqdm(range(n)):
        off = custom_onehot(np.array(list(off_list[i])))
        save_img(off,'off',i)
        tar = custom_onehot(np.array(list(tar_list[i])))
        save_img(tar,'target',i)
        
        #print (off,tar)
    return None

data = pd.read_excel('dataset-SY.xlsx')

#small = data.head()

make_images(data)



