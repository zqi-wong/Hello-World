from PIL import Image
lenna = Image.open('Lenna1bit.png')
print(lenna.mode)
print(lenna.size)
print(lenna.getbbox)
l = lenna.getdata()
for i in range(0,5):
    print(l[i])