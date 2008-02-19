while True:
    the_string = eval('"' + raw_input() + '"')
    result = ""
    lastnum = 0
    for char in the_string:
        num = ord(char)
        diff = num - lastnum
        if abs(diff) <= num:
            if diff > 0:
                result += "+" * diff
            elif diff < 0:
                result += "-" * -diff  
        else:
            result += "[-]" + "+" * num
        result += "."
        lastnum = num
    print result
