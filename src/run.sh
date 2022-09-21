
# Checks to see if python 3 is intalled
if ! [[ -x "$(command -v python3)" ]];
then
  echo "Error: 
    Python3 is not installed. please install to play"
    
  exit 1
fi
# Checks to see if rich module is intalled
if ! [[ $(pip3 freeze | grep "rich") ]];
then
  echo "Error: 
    This program utilizes the module: rich, but it looks like rich is not installed.
    Type 'pip3 install' rich to install module."
  exit 1
fi
# runs file
  python3 main.py
fi