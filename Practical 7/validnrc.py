def is_valid_nric(s):
    if len(s) != 9:
        return False
    if s[0].upper() in ['S', 'T'] and s[-1].upper() in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        for number in s[1:7]:
            if number in ['1','2','3','4','5','6','7','8','9','0']:
                return True
            else:
                return False
    
print(is_valid_nric("S2323213t"))