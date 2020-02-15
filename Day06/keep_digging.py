import zwsp_steg

with open("come_here/step-3/README.txt", "r") as f:
    encoded = f.read()
    decoded = zwsp_steg.decode(encoded)
    print(decoded)
