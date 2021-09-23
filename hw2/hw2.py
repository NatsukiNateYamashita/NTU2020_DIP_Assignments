import cv2
import numpy as np
from matplotlib import pyplot as plt





f_name = 'img/original.jpg'
src_img = cv2.imread(f_name, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('img/grayscaled.jpg', src_img)
img_hist, img_bins = np.histogram(np.array(src_img).flatten(), bins=np.arange(256+1))
cdf_original=[]
temp = 0
for v in img_hist:
    temp+=v
    cdf_original.append(temp)

equalized_img = cv2.equalizeHist(src_img)
cv2.imwrite('img/equalized.jpg', equalized_img)
equalized_img_hist, equalized_img_bins = np.histogram(np.array(equalized_img).flatten(), bins=np.arange(256+1))
cdf_equalized=[]
temp = 0
for v in equalized_img_hist:
    temp+=v
    cdf_equalized.append(temp)



fig, ax = plt.subplots()
ax.set_title('cdf_comparison')
ax.set_xlabel('Intensity')
ax.set_ylabel('# of Pixel')
ax.plot(np.arange(256), cdf_original, color='blue', label='Original')
ax.plot(np.arange(256), cdf_equalized, color='green', label='Equolized')
ax.legend(loc=0)  
plt.savefig('img/cdf_comparison.png')
# plt.show()

fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set_title('Original')
ax2.set_title('Histogram-Equalized')

ax1.set_xlabel('Intensity')
ax2.set_xlabel('Intensity')
ax1.set_ylabel('# of Pixel')
ax1.bar(np.arange(256),img_hist,color='blue', label='Original')
ax2.bar(np.arange(256),equalized_img_hist,color='green', label='Equalized')
plt.savefig('img/hist_comparison.png')
# plt.show()


# cv2.imshow('img',equalized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()