'''
Created on Dec 1, 2022

@author: pshre
'''
'''
Created on Nov 30, 2022

@author: pshre
'''
import hashlib, binascii
import time
from itertools import permutations

# utility functions
# reads a file with a list of passwords and returns a list of the passwords
def read_file(filename : str) -> list:
    with open(f'./{filename}') as f:
        lines = f.read().splitlines()
    return lines

def hash(password : str, hash_type : str) -> str:
    hashed_pwd = hashlib.pbkdf2_hmac(hash_type, password.encode('utf-8'), 'saltPhrase'.encode('utf-8'), 100)
    return binascii.hexlify(hashed_pwd)


# dict attack functions
def run_256():
    sha256_data = attack('sha256')
    sha256_data = ['SHA256', dict_length] + sha256_data
    # print('\t'+str(sha256_data)+'\n')
    return sha256_data

def run_512():
    sha512_data = attack('sha512')
    sha512_data = ['SHA512', dict_length] + sha512_data
    # print('\t'+str(sha512_data)+'\n')
    return sha512_data

def update_pass_info(passed_word : str):
    global password, pass_in_SHA256, pass_in_SHA512, pass_length
    password = passed_word
    pass_in_SHA256 = hash(passed_word, 'sha256')
    pass_in_SHA512 = hash(passed_word, 'sha512')
    pass_length = len(passed_word)

def attack(hash_type : str):
    time_car = time.time()
    
    return_list = [0, True, -1]
    data = [0, 0]
    index = 1
    while return_list[1]:
        return_list = sha256_attack(index, hash_type, time_car)
        data[1] = data[1] + return_list[0]
        index = index + 1
    data[0] = return_list[2]
    return data
    
def sha256_attack(i : int, hash_type : str, time_car) -> list:
    atk_list = []
    for tup in permutations(dict_list, i):
        word = convertTuple(tup)
        if (len(word) == pass_length):
            atk_list.append(word)
    
    index = 0;
    atk_list_len = len(atk_list)
    while (index < atk_list_len):
        if checker(atk_list[index], hash_type):
            end_time = str((time.time() - time_car))
            # cap_hash = hash_type.upper()
            return [index, False, end_time]
        else:
            index = index + 1
    return [index, True, -1]

def convertTuple(tup):
    result_str = ''
    for item in tup:
        result_str = result_str + item
    return result_str

def checker(word : str, hash_type : str):
    if hash_type == 'sha256':
        return hash(word, hash_type) == pass_in_SHA256
    elif hash_type == 'sha512':
        return hash(word, hash_type) == pass_in_SHA512
    

#ploting functions
def plot(samples):
    
    times = []
    attempts = []
    
    print('SHA256 raw data for sample will load soon')
    print('While you are waiting')
    print('think about it')
    print('when you see 0.002 in a list, it cant be the hast_type because that a string, it cant the the dict_size cause thats constant, so 0.002 attempts made before guessing the password or 0.002 seconds to guess the password')
    
    for sample in samples:
        update_pass_info(sample)
        curr_data = run_256()
        times.append(curr_data[2])
        attempts.append(curr_data[3])
    
    print(f'Times: {times}')
    print(f'Attempts: {attempts}')
    
    
    print('SHA512 raw data for sample will load soon')
    for sample in samples:
        update_pass_info(sample)
        curr_data = run_512()
        times.append(curr_data[2])
        attempts.append(curr_data[3])
    
    print(f'Times: {times}')
    print(f'Attempts: {attempts}')
    
    
# file = '20-word-list.txt'
file = '100-word-list.txt'
# file = '500-word-list.txt'
dict_list = read_file(file)
dict_length = len(dict_list)




pass_in_SHA256 = ''
pass_in_SHA512 = ''
pass_length = 0

password = input("Enter password: ")
while not (password == 'q'):
    update_pass_info(password)
    print(f'\n\tSHA256: {pass_in_SHA256}')
    print(f'\tSHA256: {pass_in_SHA512}\n')
    
    sha256_data = run_256()
    print(f'\tCracked {sha256_data[0]}: {password}')
    print(f'\tTime to crack: {sha256_data[2]}\n')
    
    sha512_data = run_512()
    print(f'\tCracked {sha512_data[0]}: {password}')
    print(f'\tTime to crack: {sha512_data[2]}\n')
    
    password = input("Enter password: ")

    
print('\nTHE END')

samples_list = ['basketball', 'cheese', 'hunter', 'monkeyprincess', 'lovely1234', 'passportpass', 'testpurplemonkey','starwarssoccermonkey']
print('')
plot(samples_list)
