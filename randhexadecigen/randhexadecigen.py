def hexadec_gen(string_length,multiplier,output = 'list',leftstr = '', rightstr='',str_seperator=','):
    """
    This function generates a string or list of random hexadecimalstrings using a user-determines length and repetition.

    Input:
    string_length = str, the length of the sampling_hexastring_length
    multiplier = int, the number of DIFFERENT hexadecimal strings to generate
    leftstr = str, any characters to be added to the left of the hexadecimal generated string
    rightstr = str, any characters to be added to the right of the hexadecimal generated string
    str_seperator = str, the seperator between the different strings if multiplier > 1

    Output = 'list','str'


    Examples:
        print hexadec_gen(6,2,'str',leftstr='%',rightstr='%')
            %3917a7%,%013fad%
        print hexadec_gen(6,2,'list')
            ['77a662', 'fbb3f8']
        print hexadec_gen(2,6,'str',str_seperator='|')
            68|08|02|c1|01|21
    """
    import random

    # defining a function that generates hexadecimal random strings:
    def hexadecs(length):
       return ''.join([random.choice('0123456789abcdf') for x in range(length)])
    # defining a function that adds the leftstr and rightstr to any string:
    def leftright_str(strng):
        return leftstr+strng+rightstr

    # depending on list or str, we generate the hexadeci-strings:
    if output=='list':
        sampling_string=[]
        for i in range(1,multiplier+1): sampling_string.append(leftright_str(hexadecs(string_length)))
    elif output=='str':
        sampling_string = '{}'.format(str_seperator).join(leftright_str(hexadecs(string_length)) for x in range(1,multiplier+1))
    else:
        raise ValueError(TypeError)

    return sampling_string