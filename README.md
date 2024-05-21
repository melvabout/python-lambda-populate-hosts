# python-lambda-populate-hosts

A lambda function to be used as part of [fairground-infrastructure](https://github.com/melvabout/fairground-infrastructure). 

Sends an ssm command to populate the /ect/hosts file on all of the running [fairground-machine-images](https://github.com/melvabout/fairground-machine-images). The command runs the python script [populate_hosts.py](https://github.com/melvabout/fairground-machine-images/blob/main/packer/files/populate_hosts.py)

## Disclaimer
No unit test :(