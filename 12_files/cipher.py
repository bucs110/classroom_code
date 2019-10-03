

def main():
    cipher_amt = 5
    fn = input("Please enter a file name:")
    infile = open(fn, "r")
    text = ""
    for aline in infile:
        for c in aline:
            if(c.isalnum()):
                text += chr(ord(c)+cipher_amt)
            else:
                text += c
    infile.close()
    outfile = open(fn+".enc", "w")
    outfile.write(text)
    outfile.close()
main()
