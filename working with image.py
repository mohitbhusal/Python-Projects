from PIL import Image

img = Image.open(r"C:\Users\mohit\Desktop\All A Olympiad\l145_23321529135463.jpg")
# Shows The info of image
print(img.format)
print(img.mode)
print(img.size)
# To Resize the image
# img.resize(450, 450)
# To rotate the image
img.rotate(5).show()
# img.show()
# img.save(r'C:\Users\mohit\Desktop\rgb.jpg')
#more is inside working with image directory

