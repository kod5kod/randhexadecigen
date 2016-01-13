# randhexadecigen
Generates a string or list of random hexadecimalstrings using a user-determines length and repetition



## hexadec_gen function:
hexadec_gen(string_length,multiplier,output = 'list',leftstr = '', rightstr='',str_seperator=','):

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
