# read the entire contents of the file
#with open("weather.csv", 'r') as reader:
#	data = reader.read()
#	print(data)

# read line by line
#with open("weather.csv", 'r') as reader:
#    data=reader.readline()
#    while data != "":
#        print data
#        data=reader.readline()

#print "No more lines"

# for loop to grab just the rainfall values
#with open("weather.csv", 'r') as reader:
#    line=reader.readline()
#    rain=[]
#    for j in reader.readlines():
#        r = j.strip().split(",")[-1]
#        R=float(r)
#        rain.append(R)

#print rain

# writing the rain list to a file called myrain
#with open("myrain.txt", 'w') as writer:
#    for i in rain:
#        writer.write(str(i) + "\n")

#reading and writing some binary data
import struct 
bin_data = struct.pack("bbbb", 123,12,45,34)
with open("mybinary.dat", "wb") as binarywriter:
    binarywriter.write(bin_data)

with open("mybinary.dat", "rb") as binaryreader:
    bin_data2= binaryreader.read()

data = struct.unpack("bbbb", bin_data2)
print data
