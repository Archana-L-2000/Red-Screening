
from simpleimage import SimpleImage # simpleimage library have to be installed (if not working properly just get the source code from github)
INTENSITY_THRESHOLD = 1.6


def greenscreen(main_filename, back_filename):
    Image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in Image:
        average = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.green>= average*INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            Image.set_pixel(x, y, back.get_pixel(x, y))
    return Image


def main():
    orginal_stop = SimpleImage("imagename1.jpg")
    orginal_stop.show()

    back_img = SimpleImage("imagename2.jpg.jpg")
    back_img.show()

    new_image = greenscreen("imagename1.jpg", "imagename2.jpg")
    new_image.show()


main()
