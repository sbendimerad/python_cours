# Define a dictionary that maps each digit character to its corresponding pattern
digit_patterns = {
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110000',
    '8': '1111111',
    '9': '1111011',
}

def print_number(num):
    digs = str(num)
    lines = ['' for _ in range(5)]
    
    for d in digs:
        # Look up the pattern for the current digit in the dictionary
        ptrn = digit_patterns.get(d, '       ')  # Default to all spaces if the digit is not in the dictionary
        segs = [[' ', ' ', ' '] for _ in range(5)]
        
        if ptrn[0] == '1':
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1':
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1':
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1':
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1':
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1':
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1':
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
        
        for lin in range(5):
            lines[lin] += ''.join(segs[lin]) + ' '
    
    for lin in lines:
        print(lin)

print_number(int(input("Enter the number you wish to display: ")))
