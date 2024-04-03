import requests
import random
from PIL import Image
from io import BytesIO
import os

def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data[0]['url']
    else:
        return None

def open_image(image_path):
    try:
        os.system(f'start {image_path}')
    except Exception as e:
        print(f"Failed to open the image: {e}")

def main():
    while True:
        user_input = input("Type 'meow' to see a random cat image (type 'exit' to quit): ")
        if user_input.lower() == 'meow':
            cat_image_url = get_cat_image()
            if cat_image_url:
                response = requests.get(cat_image_url)
                img = Image.open(BytesIO(response.content))
                image_path = 'cat_image.png'
                img.save(image_path)  # Save the image locally
                open_image(image_path)  # Open the image
            else:
                print("Failed to fetch cat image. Please try again later.")
        elif user_input.lower() == 'exit':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Type 'meow' or 'exit'.")

if __name__ == "__main__":
    main()

