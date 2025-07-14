right_passwords = 0
valid_passwords = 0

with open('Passwords.txt', 'r') as file:
    for line in file:
        policy, password = line.split(': ')
        num_range, letter = policy.split()
        min_val, max_val = num_range.split('-')
        count = password.count(letter)    
        if int(min_val) <= count <= int(max_val):
            right_passwords += 1          
        first = password[int(min_val)-1] == letter
        second = password[int(max_val)-1] == letter

        if first ^ second:
            valid_passwords += 1

print(f"Right Passwords:{right_passwords}")
print(f"Valid Passwords:{valid_passwords}")
