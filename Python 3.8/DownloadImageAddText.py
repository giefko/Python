from pynter.pynter import generate_captioned
import requests  # to get image from the web
import shutil  # to save it locally





## Set up the image URL and filename

image_url = input("Add the url for the image in jpg form you want to download: ")
filename = image_url.split("/")[-1]





# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ', filename) #It download the image in the current path
    font_path = input("Add the font path : ")
    image_path = filename




    im = generate_captioned('Add the quote you want'.upper(), image_path=image_path, size=(1080, 1350),
                            font_path=font_path, filter_color=(0, 0, 0, 40))
    im.show()
    im.convert('RGB').save('nameoftheimage.jpg')


else:
    print('Image Couldn\'t be retreived')





