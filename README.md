# Demo - Zangief

This is a Python 3.7 demo

## Requirements

* Python 3.7+
* Git

## Instructions

[Virtual Environments](#virtual-environments)

On your machine, open Terminal or Powershell or Command Prompt. Create a directory for this demo and navigate to it

```
mkdir demo
cd demo
```

### Git

Clone this repository

```
git clone https://github.com/bromega/demo-zangief.git
```

Navigate to the repository directory

```
cd demo-zangief
```

Create a branch and give it a snazzy title

```
git checkout -b balrog-is-just-mike-tyson
```

Run the file

```
python app.py ` or ` python3 app.py
```

But wait! There's an error! Something like this:

```
File "app.py", line 42
  print(f"{name}'s {args.node} is {country}")
```

or

```
File "app.py", line 1, in <module>
  import xmltodict
ModuleNotFoundError: No module named 'xmltodict'
```

That's because we are running this on the root machine and not in a virtual environment with the necessary libraries installed.

### Virtual Environments

Create the virtual environment with Python3. Check which version is the default on your root machine:

```
python --version
```

If your machine is only running Python3 or has it as the default:

```
python -m venv venv
```

If your machine runs Python2 and Python3 (for example, OSX ships with Python2 standard):

```
python3 -m venv venv
```

If you only have Python2 installed, install Python3 before proceeding.

Activate the virtual environment:

* Terminal: ` source venv/bin/activate `
* CMD.exe ` venv\Scripts\activate.bat `
* Powershell: ` venv\Scripts\Activate.ps1 `

Once inside the virtual environment, your prompt should change to whatever you named your environment (in this case "venv") for example:

```
MFVFWJN2SJ1WL:demos oliver.williams$ source venv/bin/activate
(venv) MFVFWJN2SJ1WL:demos oliver.williams$
```

### Dependencies

Install the required libraries

```
pip install -r requirements.txt
```

Now run the script

```
python app.py
```

Instead of errors you should see a print out of data

### The Script

What's going on in this script? It's reading XML data from data.xml and printing it out in the command prompt.

What does app.py print out by default?

```
Zangief's SweetMove is OrderedDict([('Country', 'USSR'), ('Flag', 'Hammer and Sickle')])
Chun Li's SweetMove is OrderedDict([('Country', 'China'), ('Flag', 'Five Stars')])
Guile's SweetMove is OrderedDict([('Country', 'USA'), ('Flag', 'Stars and Stripes')])
Ken's SweetMove is OrderedDict([('Country', 'USA'), ('Flag', 'Stars and Stripes')])
Ryu's SweetMove is OrderedDict([('Country', 'Japan'), ('Flag', 'Sun')])
E Honda's SweetMove is OrderedDict([('Country', 'Japan'), ('Flag', 'Sun')])
Blanka's SweetMove is OrderedDict([('Country', 'Brazil'), ('Flag', 'Earth')])
```

#### Step 1

Huh, that doesn't look sweet at all. Let's look at the code:

```
# 1. answer is "HomeCountry"
answer = f["HomeCountry"]
```

And how is the XML structured?

```
<Fighters>
  <Fighter name="Zangief">
    <HomeCountry>
      <Country>USSR</Country>
      <Flag>Hammer and Sickle</Flag>
```

Ok, so what happens if we call the child node "Country" instead of just the parent node "HomeCountry"? Comment out the line that's currently determining the variable "answer" and uncomment the second one:

```
# 1. answer is "HomeCountry"
#answer = f["HomeCountry"]

# 2. answer is "HomeCountry" "Country"
answer = f["HomeCountry"]["Country"]
```

Now run the script again:

```
python app.py
```

Output:

```
Zangief's SweetMove is USSR
Chun Li's SweetMove is China
Guile's SweetMove is USA
Ken's SweetMove is USA
Ryu's SweetMove is Japan
E Honda's SweetMove is Japan
Blanka's SweetMove is Brazil
Dhalsim's SweetMove is India
```

That looks better. But those aren't sweet moves, those are countries. Why is it saying SweetMove? The print command in the script says:

```
print(f"{name}'s {args.node} is {answer}")
```

Okay, so it's getting SweetMove from args.node but where is it getting "args" from? Earlier in the code we have:

```
parser = argparse.ArgumentParser()
parser.add_argument(
    "node",
    nargs="?",
    default="SweetMove",
    help="Pick one of the nodes from data.xml"
)
args = parser.parse_args()
```

The app.py script is leveraging the native Python library [argparse](https://docs.python.org/3/library/argparse.html) for determining runtime arguments. If you don't provide an argument, it will default to the value SweetMove.

One option is to change the default value to HomeCountry:

```
parser.add_argument(
    "node",
    nargs="?",
    default="HomeCountry",
    help="Pick one of the nodes from data.xml"
)
```

Now run the script:

```
python app.py
```

Output:

```
Zangief's HomeCountry is USSR
Chun Li's HomeCountry is China
Guile's HomeCountry is USA
Ken's HomeCountry is USA
Ryu's HomeCountry is Japan
E Honda's HomeCountry is Japan
Blanka's HomeCountry is Brazil
Dhalsim's HomeCountry is India
```

That looks great! But what if we're interested in more than just HomeCountry? What if we really do want to know what each person's SweetMove is without having to change the code every time?

Let's really leverage argparse here. We can call the attribute we want at runtime by passing it as an argument to the script.

```
python app.py SweetMove
```

Output:

```
Zangief's SweetMove is USSR
Chun Li's SweetMove is China
Guile's SweetMove is USA
Ken's SweetMove is USA
Ryu's SweetMove is Japan
E Honda's SweetMove is Japan
Blanka's SweetMove is Brazil
Dhalsim's SweetMove is India
```

Great, now we're determining the attribute at runtime, but we're still getting the default result (HomeCountry/Country). Let's change the active part of the code. Comment out the second "answer" line and uncomment the third one:

```
# 2. answer is "HomeCountry" "Country"
#answer = f["HomeCountry"]["Country"]

# 3. node determined by argument at runtime
answer = f[args.node]
```

Now run the script with the argument "SweetMove":

```
python app.py SweetMove
```

Output:

```
Zangief's SweetMove is 360 Piledriver
Chun Li's SweetMove is Helicopter Kick
Guile's SweetMove is Sonic Boom!
Ken's SweetMove is Shoryuken!
Ryu's SweetMove is Haduken!
E Honda's SweetMove is Sumo Missile
Blanka's SweetMove is Electricity
Dhalsim's SweetMove is Yoga Fire!
```

Yeehaw! Now we're cooking! Let's it try HomeCountry:

```
python app.py HomeCountry
```

Output:

```
Zangief's HomeCountry is OrderedDict([('Country', 'USSR'), ('Flag', 'Hammer and Sickle')])
Chun Li's HomeCountry is OrderedDict([('Country', 'China'), ('Flag', 'Five Stars')])
Guile's HomeCountry is OrderedDict([('Country', 'USA'), ('Flag', 'Stars and Stripes')])
Ken's HomeCountry is OrderedDict([('Country', 'USA'), ('Flag', 'Stars and Stripes')])
Ryu's HomeCountry is OrderedDict([('Country', 'Japan'), ('Flag', 'Sun')])
E Honda's HomeCountry is OrderedDict([('Country', 'Japan'), ('Flag', 'Sun')])
Blanka's HomeCountry is OrderedDict([('Country', 'Brazil'), ('Flag', 'Earth')])
Dhalsim's HomeCountry is OrderedDict([('Country', 'India'), ('Flag', 'Shield')])
```

Dagnabbit, now we're back to square one. Let's try it with a parent/child argument, maybe?

```
python app.py HomeCountry/Country
```

Output:

```
Traceback (most recent call last):
  File "app.py", line 36, in <module>
    answer = f[args.node]
KeyError: 'HomeCountry/Country'
```

Harrumph. We want to be able to pass both parent nodes and child nodes to the script. We could write a custom function to interpret the runtime argument, or we could search the internet for a non-standard library. Let's go with the non-standard library [dpath](https://github.com/akesterson/dpath-python).

If you're just testing out dpath, you could install dpath directly with:

```
pip install dpath
```

However, once you've determined you're going to use it going forward, you will need to add it to the requirements file for others to use in their enviroments.

In your requirements.txt file, add dpath:

```
xmltodict
dpath
```

Now from your command prompt, install the requirements.txt file again

```
pip install -r requirements.txt
```

At the top of app.py, add a line to import dpath

```
import xmltodict
import dpath
```

Now comment out the third "answer" row and uncomment the fourth one:

```
# 3. node determined by argument at runtime
#answer = f[args.node]

# 4. node determined by argument at runtime via dpath
# this demonstrates how dpath can retrieve nested keys dynamically
# i.e. "HomeCountry/Country"
answer = dpath.util.get(f, args.node)
```

Run the script with a nested node argument:

```
python app.py HomeCountry/Country
```

Output:

```
Zangief's HomeCountry/Country is USSR
Chun Li's HomeCountry/Country is China
Guile's HomeCountry/Country is USA
Ken's HomeCountry/Country is USA
Ryu's HomeCountry/Country is Japan
E Honda's HomeCountry/Country is Japan
Blanka's HomeCountry/Country is Brazil
Dhalsim's HomeCountry/Country is India
```

Great, but does it still work for SweetMove?

```
python app.py SweetMove
```

Output:

```
Zangief's SweetMove is 360 Piledriver
Chun Li's SweetMove is Helicopter Kick
Guile's SweetMove is Sonic Boom!
Ken's SweetMove is Shoryuken!
Ryu's SweetMove is Haduken!
E Honda's SweetMove is Sumo Missile
Blanka's SweetMove is Electricity
Dhalsim's SweetMove is Yoga Fire!
```

There you go! You now have a script that can return specific, nested data points from a data.xml file based on the arguments you pass at runtime.

#### Finishing Touches

Make sure all your files are saved

Add the changes to staging:

```
git add .
```

Check the status of your files and commit to make sure everything looks good:

```
git status
```

Commit the changes to your git branch with a helpful message:

```
git commit -m "added dpath to parse arguments dynamically"
```

Push the changes to your branch

```
git push
```
