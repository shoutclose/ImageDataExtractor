import cv2
import numpy as np


def ask_to_save_image(img, imgname):
    '''Asks user if current image should be saved. Useful for evaluation

    :param numpy.ndarrray img: input image to be saved
    :param string imgname: desired name of filename

    '''

    tosaveornottosave = raw_input("Save image (y/n)? : ")

    if tosaveornottosave == "y" or tosaveornottosave == "Y":
        cv2.imwrite(imgname,img)

    return


def image_metrics(gimg,displaymetrics=False):
    '''Calculate image metrics and optinally display it.
    :param numpy.ndarray gimg: grayscale input image.
    :param bool displaymetrics: prints calculated values and displays image, useful in debugging.

    :return int rows: number of rows
    :return int cols: number of columns
    :return int imgarea: pixels in image
    :return int imgmean: mean pixel intensity in image
    :return float imgstdev: standard deviation of pixel intensities
    :return float crossstdev: standard of pixel intensities across image diagonals. 

    '''

    rows = len(gimg)
    cols = len(gimg[0])
    flatgimg = gimg.flatten()
    imgarea = rows*cols
    imgmean = sum(flatgimg)/len(flatgimg)
    imgstdev = np.std(flatgimg)
    crossstdev = np.std(np.diagonal(gimg))

    if displaymetrics == True:
        print "mean: " + str(imgmean)
        print "stdev: " + str(imgstdev)
        print "area: " + str(imgarea)
        print "crossstdev: " + str(crossstdev)
        plt.hist(gimg.ravel(),256,[0,256]); plt.show()

    return rows, cols, imgarea, imgmean, imgstdev, crossstdev


def show_image(imgfilename,waitkey = 0,imgname = None,mag = None):
    '''Used to display images in cv2 format
    :param numpy.ndarray imgfilename: input image.
    :param int waitkey: miliseconds to display image, if 0 user must close manually
    :param string imgname: header while displaying image.
    :param int mag: amount to magnify image by.

    '''

    if imgname == None:
        imgname = str(imgfilename)

    if mag != None:
        imgfilename = cv2.resize(imgfilename,None,fx = mag, fy = mag)

    cv2.imshow(imgname,imgfilename)
    cv2.waitKey(waitkey)
    cv2.destroyAllWindows()
    
    return


def distance_formula(a,b):
    '''Inputs two coordinate points (x,y), outputs distance between them
    :param tuple a: (x,y) coordinate of 1st point
    :param tuple b: (x,y) coordinate of 2nd point

    :return int d: distance between two points
    '''

    d=((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

    return d

