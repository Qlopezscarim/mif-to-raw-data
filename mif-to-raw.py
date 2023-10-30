import struct
with open("FIR_INPUT.mif") as f:
    s = f.readlines()
new_string =""
for line in s:
    parts = line.split(":")
    try:
        result = parts[1].strip()
        result = result.strip(";")
        bytes_data = bytes.fromhex(result)
        ieee_float = struct.unpack('!f', bytes_data)[0]
        new_string = new_string + str(ieee_float) + "\n"
    except:
        pass

print("The following will be written to a text file (this line is not included in the file):  ")
print(new_string)
print("END OF FILE (this line is not included in the file)")
text_file = open("Output.txt", 'w')
text_file.write(new_string)