import time

while True:
	# Sleep for 1 second
	time.sleep(1)
	# Open image-service.txt
	with open("image-service.txt", "r+") as f:
		# if(read image-service.txt == type(number))
		read_data = f.read()
		if read_data != '':
			print("Generating random image...")
			if read_data.isnumeric():
				# copy number to local variable
				num = int(read_data)
				# Use Mod operator to mod number with number of images
				num = num % 6
				# Write path (ex : /users/cs361-images/{number}.jpg) to image-service.txt
				f.seek(0)
				f.truncate()
				file_path = 'Users/Casey/Documents/GitHub/CS361/images/'
				file_path+=str(num)
				file_path+='.jpg'
				print("Image file path: ", file_path)
				f.write(file_path)
			# Close file image-service.txt
			f.close()
			break
		else:
			#f.close()
			continue