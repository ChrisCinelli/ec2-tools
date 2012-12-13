# ec2-tools
## here they are, so very awesome for you

### to setup
if you're using pip:

    `pip install -r requirements.txt`

if you're not:

    [use pip](http://pypi.python.org/pypi/pip)


### to use
    python make-ssh-config.py --id-file-dir <where yo key files at> >> ~/.ssh/config

### what it do
outputs a portion of an ssh config file specifying the appropriate key and user for each host. this will say you maybe 20 keystrokes every 3 hours, i recon.
