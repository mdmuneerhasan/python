import cv2
import matplotlib.pyplot as plt

img=cv2.imread('dog.png')

img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


plt.imshow(img)
plt.savefig("graph1")

# plt.clf()
# plt.imshow(img2)
#
# plt.savefig("graph2")

