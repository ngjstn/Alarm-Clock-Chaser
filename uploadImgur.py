from auth import authenticate
 
image_path = '/home/pi/Desktop/image.jpg'

def upload(client):

	print("Uploading image... ")
	image = client.upload_from_path(image_path, anon=False)
	print("Done")
	print()

	return image


def uploadImg():
	client = authenticate()
	image = upload(client)
	print("Link: {0}".format(image['link']))
	
	return image['link']
