import time
import random
import matplotlib.pyplot as plt

def show_img(url):
	a = plt.imread(url)
	plt.imshow(a)
	plt.show()

if __name__ == "__main__":	
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
				time.sleep(5)
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
				time.sleep(10)
				f.close()

			with open("image-service.txt", "r+") as f:
				# Read and output image-s1ervice.txt
				randNum = f.read()
				print("Random integer in image-service.txt:", randNum)
				time.sleep(5)
				# Close image-service.txt
				f.close

			with open("image-service.txt", "r+") as f:
				# Read and output image-s1ervice.txt
				file_path = f.read()
				print("Image file path:", file_path)
				show_img(file_path)
				# Close image-service.txt
				f.close
			break

		elif int(input) ==2:
			break
		else:
			print("Unknown option")
			break 
