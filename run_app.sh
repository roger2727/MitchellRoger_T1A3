
# Checks to see if python 3 is intalled
if ! [[ -x "$(command -v python3)" ]];
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' 
  exit 1
fi
# Checks to see if rich module is intalled
if ! [[ $(pip3 freeze | grep 'rich') ]];
then
  echo 'Error: 
    This program utilizes the module: rich, but it looks like rich is not installed.
    Type "pip3 install colorama" to install module.'
  exit 1
fi
# runs file
  python3 main.py
fi