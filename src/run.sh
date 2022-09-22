package=(rich==12.5.1)
# checks if you are in a virtualenv
if [[ "$VIRTUAL_ENV" == "" ]]; then 
    echo "You are not in a working virtualenv";
    echo "type python3 -m venv venv"
    echo "than . venv/bin/activate "

    exit 1
fi 
# checks if package is installed
if [[ "$package" != "" ]]; then
    echo "Error: 
    This program utilizes the module: rich, but it looks like rich is not installed.
    do you what to install the package y or n"
    read answer
     if [[ "$answer" ==  "y"  ]]; then 
     pip install "${package[@]}";
     else
     echo "you need rich package to play"
fi     

# runs file
  python3 main.py
fi