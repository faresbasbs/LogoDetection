
def Fix_Image(path):
    from PIL import Image
    import math

    foo = Image.open(path)  # My image is a 200x374 jpeg that is 102kb large
    #foo.size  # (200, 374)
    len, wid = foo.size

    area = len*wid
    factor = math.sqrt(90000/area)
#    print(len,wid,area)
    #exit(0)

    nlen = math.floor(len*factor)
    nwid = math.floor(wid*factor)

    # downsize the image with an ANTIALIAS filter (gives the highest quality)
    foo = foo.resize((nlen,nwid))

    #foo.save('path/to/save/image_scaled.jpg', quality=95)  # The saved downsized image size is 24.8kb

    foo.save(path, optimize=True, quality=95)  # The saved downsized image size is 22.9kb
