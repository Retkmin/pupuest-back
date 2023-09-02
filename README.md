# Pupuest will be a project to automate testing of a tarding startegy

This will be the backend that integrate data feed from the front, integrate the trading view and expose the Api.

### The road map will be:

    - Integration with Trading View
    - Read ops from fronted app
    - Integration with Power BI
    - Integrate ML 
    - Generate atomatic BT


### Requirements
 - Python 3.11
 - Pip, for package management

Make sure Windows Defender doesn't block some of these actions.
Make sure PowerShell has the execute scripts policy permited.
### To install the project
We will work with virtual environments, to manage the virtual environment, we need to install the package virtualenv:
    pip install virtualenv

Now we procede to create a virtual environment for the project. To do so we use the next command:
    python -m venv <virtual_environment_config_folder_name>

Once the virtual environment is created, we need to activate it, to do so we need to execute a file called "activate" or "Activate" or "Activate.ps1", it's inside the folder "Scripts" inside the folder containing all the virtual environment config and files.
    <virtual_environment_config_folder_name>\Scripts\activate

Now we need to install all the necesary dependencies inside the virtual environment we just created and activated, to do so, use the next command:
    pip install -r requirements.txt

If all the dependencies have been installed, we can no launch the backend.
### To launch the backend
Once everything is installed properly, we can run the backend using the next command, we can also change the port with the extra argument --port <port_number>
    uvicorn main:app --reload

The default address is http://127.0.0.1:8000, but you can check it on the terminal.
To see the docs we go to http://127.0.0.1:8000/docs.