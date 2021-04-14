import json
import sys
from client import * 

ID = "n3eEadyA2H45SSH97P9JCgWFqajNk8pvx086l1tVwFCEs9sPkT"

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        try:
            vectors = json.load(file)
            for vector in vectors:
                if len(vector) != 11:
                    print("Error!")
                else:
                    res = submit(ID, vector)
                    print(res)
            print("Parsed Succesfully!")
        except json.decoder.JSONDecodeError:
            print("Decoding JSON has failed.")
    file.close()

