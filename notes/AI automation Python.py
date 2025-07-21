AI automation Python
===========================

=========================OS===============
Kernel
user space

managing files and processing.

major os: windows, mac os, Linux (business os)

Linux (total boss)
------------------
huge community effort
it is open source
ex: ubuntu,debian, redhat
android is also in Linux
Linux is based on unix principles.

-------------Installing python------------
pip is command line tool commonly used to install ,update or remove external python modules

In windows
-----------
download executable python for windows and run 
and test on cmd
python --version

>python
>>>import requests (it gives some error)
>>>exit(ctrl+z)
>pip install requests

>python
>> import requests
>> response = requests.get("http://www.google.com"")
>> len(response.text)
17365

in macos
-----------
homebrew (download from website)
run and check

in Linux
----------
python --version
By default it comes with python here it shows python 2
python3 --version
if exists it shows 
if not need to install
apt(Debian)
yum(redhat)

sudo apt install python3-pil


pandas module
---------------
pip install pandas
python
>> import pandas
>> visitors=[232,324]
>> err = [33,11]
>> df = pandas.DataFrame({"visitors":visitors,"err":err},index=["Mon","Tues"]
>> df["err"].mean()


to save the python code in file hello.py
print("Hello world")

to execute python hello.py
Hello world

to save and run the file to run using python3, the first line should be as follows:
#!/usr/bin/env python3

to change the permissions of the file 
chmod +x hello.py

./hello.py  (this is equivalent to python3 hello.py)


purpose of using a shebang line in a Python file
	Keep it up! Inserting a shebang line (such as #!/usr/bin/env python3) as the first line tells the operating system what command we want to use to execute the script.

