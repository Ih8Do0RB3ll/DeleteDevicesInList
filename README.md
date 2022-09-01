# DeleteDevicesInList
Helps to automate device deletion from ur windows PC

If you've met with the same problem having over a 100 scanner devices which were installed from the network you can simply use this script to automate deletion of this useless devices

I don't know how to write readme's so bear with me and my poor grammar :P

First of all we need to get list of devices you want to delete and you can do it with pnputils
```
pnputil /enum-interfaces
```
get ids of devices you want to delete
I had similiar scanners and their ids looked like 

SWD\DAFWSDProvider\urn:uuid:cfe92100-67c4-11d4-a45f-9caed3b038b3
SWD\DAFWSDProvider\urn:uuid:cfe92100-67c4-11d4-a45f-9caed3b038c3
SWD\DAFWSDProvider\urn:uuid:cfe92100-67c4-11d4-a45f-9caed3b038c5
SWD\DAFWSDProvider\urn:uuid:cfe92100-67c4-11d4-a45f-9caed3b038c6

so I had something to work with, cuz "urn:uuid:cfe92100-67c4-11d4-a45f-" is similiar for all of them

Next we need to get file with all of the interface IDs we want to delete: 
```
pnputil /enum-interfaces | findstr "insert common part of device IDs here" > "%homepath%\Desktop\filename.txt"
```
edit output file so you only have IDs there

run python script from cmd with administrator rights: 
```python "path to script" ```or launch it from any IDLE with administrator rights.

Let it do it's job

By any means im not to be blamed if you break/delete something. 
