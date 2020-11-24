from PIL import Image

def img_to_gray(image_path):
	input_image = Image.open(image_path)

	output_image = input_image.convert('L')

	output_image.save(image_path)
