import sys
from PIL import Image, ImageOps

def main():
    try:
        check_args()
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        process_image(input_image, output_image)
    except FileNotFoundError:
        sys.exit("File not found")


def process_image(input_image, output_image):
    shirt = Image.open("shirt.png")
    input_image = Image.open(input_image)
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)
    input_image.paste(shirt, box = (0, 0), mask = shirt)
    input_image.save(output_image, format=None)


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_extensions = (".jpg", ".jpeg", ".png")
    if not (sys.argv[1].endswith(valid_extensions) and sys.argv[2].endswith(valid_extensions)):
        sys.exit("Not an acceptable image file")

    ext1 = sys.argv[1].rsplit('.', 1)[-1].lower()
    ext2 = sys.argv[2].rsplit('.', 1)[-1].lower()
    if ext1 != ext2:
        sys.exit("Files do not have the same extension")

if __name__ == "__main__":
    main()
