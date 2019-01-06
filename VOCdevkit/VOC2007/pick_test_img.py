import glob
import os
import shutil

def pick_testimg(dest_path,test_path,img_path):
    if os.path.exists(dest_path)==False:
        os.mkdir(dest_path)

    test_img = glob.glob(test_path)
    for img in test_img:
    	f = open(img,'r')
    	img_names = f.readlines()
    	f.close()
    for i in range(len(img_names)):
    	img_name = img_names[i].split('\n')[0]+'.jpg'
    	from_path = os.path.join(img_path,img_name)
	to_path = os.path.join(dest_path,img_name)
	shutil.copy(from_path,to_path)

if __name__ == '__main__':
    dest_path = './TestImages'
    test_path = './ImageSets/Main/test.txt'
    img_path = './JPEGImages'
    pick_testimg(dest_path,test_path,img_path)

