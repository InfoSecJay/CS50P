import sys
from PIL import Image

def main():
    try:
        print("Hello")
        check_args()
        input_image = sys.argv[1] 
        output_image = sys.argv[2]
        process_image(input_image, output_image)
    except FileNotFoundError:
        sys.exit("File not found")


def process_image(input_image, output_image):
    img = Image.open(input_image)
    shirt = Image.open("shirt.png")
    print("success")
    # size = shirt.size
    # photo.paste(shirt, shirt)
    print(img.size)
    print(shirt.size)
    
    # crop the benfore.img 


def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not ((sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpeg")) and (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png") or sys.argv[2].endswith(".jpeg"))):
        sys.exit("Not an acceptable image file")
        
        
        
        
if __name__ == "__main__":
    main()