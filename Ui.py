import time
import random

while True:
	#1 to generate new image or 2 to exit
	print("Enter 1 to generate a new image or 2 to exit")
	input = input()
	if int(input) == 1:
		# Open prng-service.txt
		with open("prng-service.txt", "r+") as f:
			print("Opening prng-service.txt")
			# Read file
			f.read()
			#read_data = f.read()
			# Write “run” in prng-service.txt
			f.write("run")
			# Sleep for 5 seconds 
			f.close()
			time.sleep(5)

		with open("prng-service.txt", "r+") as f:
			# Read pseudo random number from prng-service.txt
			read_data = f.read()
			print("Random integer (1-99):", read_data)
			f.close()

		# Open image-service.txt
		with open("image-service.txt", "r+") as f:
			# Read file
			f.read()
			print("Opening image-service.txt")
			# Erase data in image-service.txt
			f.seek(0)
			f.truncate()
			# Write pseudo random number
			f.write(read_data)
			# Sleep for 5 seconds 
			time.sleep(5)
			f.close()

		with open("image-service.txt", "r+") as f:
			# Read and output image-s1ervice.txt
			read_data2 = f.read()
			print("Random integer in image-service.txt:", read_data2)
			time.sleep(5)
			# Close image-service.txt
			f.close

		with open("image-service.txt", "r+") as f:
			# Read and output image-s1ervice.txt
			read_data3 = f.read()
			print("Image file path:", read_data3)
			# Close image-service.txt
			f.close
		break

	elif int(input) ==2:
		break
	else:
		print("Unknown option")
		break 
