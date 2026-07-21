#Write a program to input any alphabet and check whether it is vowel or consonant. 

n = input('Enter the alphabet:')

if n in 'aeiouAEIOU':
    print('The alphabet is vowel')
else:
    print('The alphabet is consonant')