# non-native libraries
import xmltodict
import dpath

# native libraries
import argparse


# initialize argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "node",
    nargs="?",
    default="SweetMove",
    help="Pick one of the nodes from data.xml"
)
args = parser.parse_args()


if __name__ == '__main__':
    file = open("data.xml").read()
    data = xmltodict.parse(file)
    fighters = data["Fighters"]["Fighter"]

    for f in fighters:
        name = f["@name"]

        # 1. country is "HomeCountry"
        # answer = f["HomeCountry"]

        # 2. country is "HomeCountry" "Country"
        # answer = f["HomeCountry"]["Country"]

        # 3. node determined by argument at runtime
        # answer = f[args.node]

        # 4. node determined by argument at runtime via dpath
        # this demonstrates how dpath can retrieve nested keys dynamically
        # i.e. "HomeCountry/Country"
        answer = dpath.util.get(f, args.node)

        # as of Python 3.6 or higher you can use f-strings
        # to insert variables into strings
        print(f"{name}'s {args.node} is {answer}")
