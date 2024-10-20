# Program to convert a code into a string containing only the space characters like tab, space
# Program will replace each character in the code with spaces equal to that to its ascii value
# meaning 'a' will be replaced by 65 white spaces and 'A' will be separated by 91 white spaces
# and each character will be separated by tab character or '\t'

data : str = ""
encoded_data = []
with open("c:\\Projects\\Summer_training\\code_for_invisible_code.py","r") as f:
    data = f.read()
    encoded_data = [ " "*ord(x) for x in data ]
    encoded_data = "\t".join(encoded_data)

print('-'*50,"\nEncoded data is : \n",encoded_data, '\n', '-'*50, sep = "")

# For decoding the data
decoded_data = "".join([ chr(len(x)) for x in encoded_data.split("\t") ])
print('-'*50,"\nDecoded data is : \n",decoded_data,'\n', '-'*50, sep = "")