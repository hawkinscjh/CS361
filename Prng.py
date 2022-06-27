import time
import random

while True: 
	# Sleep for 1 second.
    time.sleep(1)

    # Open file prng-service.txt
    #f = open('prng-service.txt', 'w', encoding='utf-8')
    with open("prng-service.txt", "r+") as f:
        # Read file
        read_data = f.read()
        print(read_data)
        # If line in file is “run”:
        if read_data == 'run':
            # Generate random number 
            randNum = random.randint(1,99)
            # Erase “run” from prng-service.txt
            f.seek(0)
            f.truncate()
            # Write random number in to prng-service.txt
            f.write(str(randNum))
            # Close file 
            f.close()
            break
        else:
            # print("Error: 'run' not found in .txt file")
            # Close file 
            # f.close()
            #break
            print("Waiting for run")
            f.close()
            continue
        
