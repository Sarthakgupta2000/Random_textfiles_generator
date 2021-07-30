""" 
    # Random text file generator


    To use :- python Randomtextfilegenerator.py "target_directory" number_of_file file_size_in_mb

    this python script generates 'n1' text files with 'n' bytes of data

    Data will be generated once and then passed to function in each call to be copied to every txt files,so this saves time

 """

import os.path
import numpy as np
import time
import argparse

# this is a generator function and yields file path name 
def create_test_files(target_dir, content, n1, template="file_%s.txt"):
    for i in range(n1):
        path = os.path.join(target_dir, template % i)  # string formatting
        with open(path, 'w') as fh:
            fh.write(content)
        # from the function continue without destroying states of local variables
        # and continue execution from last yield statement
        yield path

def main(target_dir, num_files, file_size):
    start_time = time.time()

    # generating a numpy array of small alphabet letters
    letters = np.array(list(chr(ord('a') + i) for i in range(26)))

    # n -> number of bytes, each character equals 1 byte
    n = (1024 ** 2) * file_size

    #create a sample of 'n' number of characters 
    chars = ''.join(np.random.choice(letters, n))

    # chars = np.random.choice(letters, n)
    end_time = time.time()
    print("time taken to create random text data(once)", end_time - start_time)

    start_time = time.time()
    
    # iterating through generator function and printing file path name
    # arguments are target directory and data to be copied in each file 
    for file_name in create_test_files(target_dir, chars, num_files):
        print(file_name)
    end_time = time.time()
    print("time taken to write data to files", end_time - start_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("target_dir")
    parser.add_argument("number_of_files", type=int)
    parser.add_argument("size_of_each_file_in_mb", type=int)
    args = parser.parse_args()
    main(args.target_dir, args.number_of_files, args.size_of_each_file_in_mb )
