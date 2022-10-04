import numpy as np
from PIL import Image #Pillow 패키지의 Image 라이브러리를 불러오는 방법

image = Image.open("week05/dip_for_numpy/images/img_041.png")
print(type(image)) #이미지 파일 타입 확인

image.show() #화면에 이미지 출력

img_np = np.array(image) #numpy 배열로 변환
#numpy 변환시 필수적으로 확인해야 할 4가지
#1. dtype
#2. shape
#3. size
#4. ndim

print(img_np.shape, img_np.shape, img_np.size, img_np.ndim) #numpy 배열 정보 확인

#numpy 배열정보를 pillow패키지 이미지로 변환하는 방법:
image2 = Image.fromarray(img_np)
print(type(image2))
image2.show()
#numpy 배열정보를 이미지로 출력하는 과정은 Matplotlib를 더 자주 사용한다.

path = "week05/"

#이미지 배열정보를 파일로 저장하는 방법:
image2.save(path+'test.bmp','bmp') # 객체.save(파일명, 확장자)

#사진 정보:
print(image.mode) #색역정보
print(image.size) #사이즈 정보


#------------------------------#

#R,G,B Split:
img_np = np.array(image)
print(img_np.shape)
R = img_np[:,:,0]
G = img_np[:,:,1]
B = img_np[:,:,2]
print(R.shape)
print(G.shape)
print(B.shape)

#R, G, B로 분리한 채널을 합치는 방법:
#zeros 3차원 배열 생성
img_c = np.zeros((680,1024,3), dtype=np.uint8) #dtype을 unit8로 지정해줘야만 한다.
#인덱스에 R,G,B 삽입
img_c[:,:,0] = R
img_c[:,:,1] = G
img_c[:,:,2] = B

img_back = Image.fromarray(img_c)
img_back.show()