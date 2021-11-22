def solution(new_id):
    answer = ''
    allowed_char =["-","_","."]
    new_string=''
    
    # step 1 Aphabet change
    new_id = new_id.lower()
    # stem 2 Delete special character
    for char in new_id:
        if (char.isalnum() == False) and char not in allowed_char: 
            new_string=new_string
        else:
            new_string += (char)
    # step 3 ... change
    print(new_string)
    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
print(new_id)
print(solution(new_id))