# Importing library
import cv2
from pyzbar.pyzbar import decode


# Make one method to decode the barcode
def BarcodeReader(image):
	
	# making sure to read the barcode image in numpy array using cv2
	img = cv2.imread(image)
	
	# Decoding the barcode image
	detectedBarcodes = decode(img)
	
	# printing a message when a barcode is not detected
	if not detectedBarcodes:
		print("Barcode Not Detected or your barcode is blank/corrupted!")
	else:
	
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes:
		
			# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to heighlight the barcode
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10),
						(255, 0, 0), 2)
			
			if barcode.data!="":
			
			# Printing the barcode data
				print(barcode.data)
				print(barcode.type)
				
	#Display the image
	cv2.imshow("Image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
# Take the image from user
	image="Img.jpg"
	BarcodeReader(image)

#Suvariya, B (2021) GeeksforGeeks [source code]. https://www.geeksforgeeks.org/how-to-make-a-barcode-reader-in-python/