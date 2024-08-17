import cv2
import numpy

img = cv2.imread("image.jpg")
cam = cv2.VideoCapture(0)
res, frame = cam.read()

def getAvrgBrightnessVal(image = cv2.Mat,size = 5):
    HEIGHT, WIDTH = image.shape
    print(HEIGHT, WIDTH)
    mat1 = []
    col = []
    avrg = 0
    for i in range(0,HEIGHT):
        for j in range(0,WIDTH):
            avrg += image[i][j]
            if (j+1) % size == 0:
                avrg /= size
                col.append(avrg)
                avrg = 0
        mat1.append(col)
        col = []
        
    mat2 = []
    avrg = 0
    for j in range(0,int(WIDTH/size)):
        col = []
        for i in range(0,HEIGHT):
            avrg += mat1[i][j]
            if (i+1) % size == 0:
                avrg /= size
                col.append(avrg)
                avrg = 0
        mat2.append(col)
    
    return mat2
   

def getLetterByBrightness(brightness):
    letters = " .:-=+*#%@"
    if brightness > 255:
        return " "         
    index = int((brightness/255)*(letters.__len__())) - 1
    return letters[index]

img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cvrt_img = getAvrgBrightnessVal(img,5)

for j in range(0,cvrt_img[0].__len__()):
    for i in range(0,cvrt_img.__len__()):
        print(getLetterByBrightness(cvrt_img[i][j]),end="")
    print()

# cv2.imshow("dsad",img)
cv2.imshow("cam",frame)
cv2.waitKey()



cv2.destroyAllWindows()