def main():
    codes = {"A" : "=", "a" : "+", "B" : "-", "b" : "_", "C" : "0", "c" : ")", "D" : "9", "d" : "(", "E" : "8", "e" : "*", "F" : "7", "f" : "&", "G" : "6", "g" : "^", "H" : "5", "h" : "%", "I" : "4", "i" : "$", "J" : "3", "j" : "#", "K" : "2", "k" : "@", "L" : "1", "l" : "!",
             "M" : "]", "m" : "}", "N" : "[", "n" : "{", "O" : "/", "o" : "?", "P" : ".", "p" : ">", "Q" : ",", "q" : "<", "R" : "`", "r" : "~", "S" : "a", "s" : "A", "T" : "b", "t" : "B", "U" : "c", "u" : "C", "V" : "d", "v" : "D", "W" : "e", "w" : "E", "X" : "f", "x" : "F",
             "Y" : "g", "y" : "G", "Z" : "h", "z" : "H", " " : " "}
    list_of_keys = list(codes)
    infile = open("DictionaryEncryptionHW\info_security.txt", "r")
    outfile = open("encryption.txt", "w")
    for line in infile:
        for c in line:
            for key in list_of_keys:
                if c == key:
                    c = codes[key]
                    outfile.write(c)
    outfile.close()
    infile.close

main()