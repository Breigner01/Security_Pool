import sys

def main():
    try:
        string_to_decode = list(sys.argv[1])
        string_len = len(sys.argv[1])
        if sys.argv[2] == "bruteforce":
            bruteforce(string_to_decode, string_len)
        else:
            gap = int(sys.argv[2])
            one_gap(string_to_decode, string_len, gap)
    except:
        helps()
        exit(84)

def helps():
    print("DESCRIPTION:")
    print("\tpython3 caesar.py string gap\n")
    print("USAGE:")
    print("\tstring\tthe string you intend to decode")
    print("\tgap\tthe gap you want to have between the coded and decoded string")
    print("\t\tyou can give bruteforce to try every possibilities")

def bruteforce(string_to_decode, string_len):
    for gap in range(1, 26):
        string_to_decode = list(sys.argv[1])
        one_gap(string_to_decode, string_len, gap)

def one_gap(string_to_decode, string_len, gap):
    for i in range(string_len):
        if string_to_decode[i] >= 'A' and string_to_decode[i] <= 'Z' and chr(ord(string_to_decode[i]) + gap) > 'Z':
            string_to_decode[i] = chr(ord(string_to_decode[i]) + gap - 26)
        elif string_to_decode[i] >= 'a' and string_to_decode[i] <= 'z' and chr(ord(string_to_decode[i]) + gap) > 'z':
            string_to_decode[i] = chr(ord(string_to_decode[i]) + gap - 26)
        else:
            string_to_decode[i] = chr(ord(string_to_decode[i]) + gap)
    print("Gap of (" + '%d'%gap + "):")
    print(''.join(string_to_decode) + '\n')

if __name__ == '__main__':
    main()