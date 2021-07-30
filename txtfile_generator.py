# Random text file generator
# this python script generates 'n1' text files with size of 'n' mb of data
import os.path
import numpy as np
import time


def create_test_files(target_dir, content, n1=5000, template="file_%s.txt"):
    """  Generator function
         argument list - n1=number of files """
    for i in range(n1):
        path = os.path.join(target_dir, template % i)  # string formatting
        with open(path, 'w') as fh:
            fh.write(content)
        #  from the function without destroying states of local variables
        # and continue execution from last yield statement
        yield path

def main():
    start_time = time.time()
    letters = np.array(list(chr(ord('a') + i) for i in range(26)))
    n = (1024 ** 2)
    chars = ''.join(np.random.choice(letters, n))
    # chars = np.random.choice(letters, n)
    end_time = time.time()
    print("time taken to create random text data(once)", end_time - start_time)

    start_time = time.time()
    for file_name in create_test_files("multiple_random_textfiles", chars):
        print(file_name)
    end_time = time.time()
    print("time taken to write data to files", end_time - start_time)

if __name__ == '__main__':
    main()
