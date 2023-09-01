# Pupuest will be a project to automate testing of a tarding startegy

This will be the backend that integrate data feed from the front, integrate the trading view and expose the Api.

### The road map will be:

    - Integration with Trading View
    - Read ops from fronted app
    - Integration with Power BI
    - Integrate ML 
    - Generate atomatic BT

### To install the project
We need to create a virtual environment for the project. Be careful, Windows Defender might be blocking the acceso of python.exe to the folder. To do so we use the next command:
    python -m venv <virtual_environment_config_folder_name>

Once the virtual environment is created, we need to activate it, to do so we need to execute a file called "activate" or "Activate" or "Activate.ps1", it's inside the folder "Scripts" inside the folder containing all the virtual environment config and files.
    
    <virtual_environment_config_folder_name>\Scripts\activate

In windows you might need to enable the policy to execute scripts from PowerShell:

    ### Pending to add

Now we need to install all the necesary dependencies inside the virtual environment we just created and activated, to do so, use the next command:
    pip install -r requirements.txt

### To launch the backend
Once everything is installed properly, we can run the backend using the next command, we can also change the port with the extra argument --port <port_number>
    uvicorn main:app --reload

The default address is http://127.0.0.1:8000, but you can check it on the terminal.