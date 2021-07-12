def is_valid_nric(s): # regex moment
    if len(s) != 9:
        return False
    if s[0].upper() in ['S', 'T'] and s[-1].isalpha():
        for number in s[1:7]:
            if number.isnumeric():
                return True
            else:
                return False
    
print(is_valid_nric("S2323213t"))