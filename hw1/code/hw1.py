import sys
import cv2
import time
import matplotlib.pyplot as plt


def myresize_1(img, method, save_fname):
    if method == 'linear':
        img = cv2.resize(img, dsize=None, fx=0.1, fy=0.1, interpolation = cv2.INTER_LINEAR)
    elif method == 'cubic':
        img = cv2.resize(img, dsize=None, fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_fname, img)
    print('SAVED {} !'.format(save_fname))

def myresize_2(img, method, scale, save_fname):
    if method == 'linear':
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale, interpolation = cv2.INTER_LINEAR)
    elif method == 'cubic':
        img = cv2.resize(img, dsize=None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_fname, img)
    print('SAVED {} !'.format(save_fname))
    
def myresize_3(img, height, width, save_fname):
    img = cv2.resize(img, dsize=(width, height))
    cv2.imwrite(save_fname, img)
    print('SAVED {} !'.format(save_fname))

# def myresize_3_mod(img, height, width, save_fname, method):
#     if method == 'linear':
#         img = cv2.resize(img, dsize=(width, height), interpolation = cv2.INTER_LINEAR)
#     elif method == 'cubic':
#         img = cv2.resize(img, dsize=(width, height), interpolation = cv2.INTER_CUBIC)
#     # img = cv2.resize(img, dsize=(width, height))
#     cv2.imwrite(save_fname, img)
#     print('SAVED {} !'.format(save_fname))


def mygettime(img, method, scale, num_of_times):
    if scale == 0:
        avg_t = 0
    else:
        src_img = img
        total_t = 0
        for i in range(num_of_times):
            start_t = time.time()
            if method == 'linear':
                img = cv2.resize(src_img, dsize=None, fx=scale, fy=scale, interpolation = cv2.INTER_LINEAR)
            elif method == 'cubic':
                img = cv2.resize(src_img, dsize=None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
            end_t = time.time()
            total_t += end_t - start_t
        avg_t = total_t / num_of_times
    print('Method: {}, Scale: {}'.format(method,scale))
    return avg_t




########## set task number ##########
try:
    task = sys.argv[1]
except:
    print("Error: Please give a number of the task as an argument.")
    print("Ex: hw1.py 1")
    exit()

########## set params ##########
src_img = cv2.imread(r'../img/original.jpg')
method_list = ['linear','cubic']

########## set params for task 2 ##########
scale_list = [0.1, 5.0, 30]

########## set params for task 3 ##########
height, width, channel = src_img.shape

########## set params for task 4 ##########
scale_list_for_gettime = [i/10 for i in range(0,101,2)]
num_of_times = 50

########## processing ##########
if task == '1':
    for method in method_list:
        fname = '../img/{}.jpg'.format(method)
        myresize_1(src_img, method, fname)

elif task == '2':   
    for method in method_list:
        for scale in scale_list:
            fname = '../img/{}_{}.jpg'.format(method,scale)
            myresize_2(src_img, method, scale, fname)

elif task == '3':
    for method in method_list:
        for scale in scale_list:
            fname = '../img/{}_{}.jpg'.format(method,scale)
            save_fname = '../img/resized_{}_{}.jpg'.format(method,scale)
            img = cv2.imread(fname)
            myresize_3(img, height, width, save_fname)
           

elif task == 'diff':
    for scale in scale_list:
        linear_fname = '../img/{}_{}.jpg'.format(method_list[0],scale)
        cubic_fname = '../img/{}_{}.jpg'.format(method_list[1],scale)
        save_fname = '../img/diff_{}.jpg'.format(scale)
        img_linear = cv2.imread(linear_fname)  
        img_cubic = cv2.imread(cubic_fname)  
        diff = img_linear - img_cubic
        # resize img to the size of original because Atom markdown extention does not work for the largest images
        resized_diff = cv2.resize(diff, dsize=(width, height))
        cv2.imwrite(save_fname, resized_diff)
        print('SAVED {} !'.format(save_fname))

elif task == 'edge':
    for method in method_list:
        for scale in scale_list:
            fname = '../img/{}_{}.jpg'.format(method,scale)
            save_fname = '../img/edge_{}_{}.jpg'.format(method,scale)
            gray_img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
            if scale == 0.1:
                thho1 = 480
                thho2 = 100
            elif scale == 5.0:
                thho1 = 40
                thho2 = 25
            elif scale == 30:
                thho1 = 7
                thho2 = 4
            else:
                print('ERROR! The value of scale may be wrong!')
            canny_img = cv2.Canny(gray_img, thho1, thho2)
            # resize img to the size of original because Atom markdown extention does not work for the largest images
            resized_canny = cv2.resize(canny_img, dsize=(width, height))
            cv2.imwrite(save_fname, resized_canny)
            print('SAVED {} !'.format(save_fname))

elif task == '4':
    avg_t_list = []
    for method in method_list:
        tmp = []
        for scale in scale_list_for_gettime:
            tmp.append(mygettime(src_img, method, scale, num_of_times))
        avg_t_list.append(tmp)
    fig, ax = plt.subplots()
    ax.set_xlabel('scale')
    ax.set_ylabel('average time')
    ax.grid()
    ax.plot(scale_list_for_gettime, avg_t_list[0], color='blue', label='bilinear')
    ax.plot(scale_list_for_gettime, avg_t_list[1], color='green', label='bicubic')
    ax.legend(loc=0)  
    plt.savefig('../img/time_complexity_comparison.png')

else:
    print("Error: Please give a number of the task as an argument.")
    print("Ex: hw1.py 1")





