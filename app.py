import xmltodict
import dpath
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "field",
    nargs="?",
    default="SweetMove",
    help="Pick one of the fields from data.xml"
)
args = parser.parse_args()



if __name__ == '__main__':
    file = open("data.xml").read()
    data = xmltodict.parse(file)
    fighters = data["Fighters"]["Fighter"]

    for f in fighters:
        name = f["@name"]

        # country is "HomeCountry"
        #country = f["HomeCountry"]

        # country is "HomeCountry" "Country"
        #country = f["HomeCountry"]["Country"]

        # country is dpath "HomeCountry/Country"
        #country = dpath.util.get(f, "HomeCountry/Country")

        # field determined by argument at runtime
        #country = f[args.field]

        # field determined by argument at runtime via dpath
        # this demonstrates how dpath can retrieve nested keys dynamically
        country = dpath.util.get(f, args.field)

        # as of Python 3.7 you can use f-strings
        # to insert variables into strings
        print(f"{name}'s {args.field} is {country}")
