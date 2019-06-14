# Demo - Zangief

This is a python 3.7 demo

### Requirements

Python 3.7

### Instructions

Clone this repository

` git clone https://github.com/bromega/demo-zangief.git `

Create a branch and give it a snazzy title

` git checkout -b balrog-is-just-mike-tyson`

Run the file but oops there's an error

` python app.py `

or

` python3 app.py `

Wait there's an error!

```
File "app.py", line 42
  print(f"{name}'s {args.field} is {country}")
```

or

```
File "app.py", line 1, in <module>
  import xmltodict
ModuleNotFoundError: No module named 'xmltodict'
```

That's because we are running this on the root machine and not in a virtual environment with the necessary libraries installed.

Create the virtual environment

` python3 -m venv venv `

Activate the virtual environment

` source venv/bin/activate `

Install the required libraries

` pip install -r requirements.txt `
