# CP2020-controller
Code to control a Flann microwave CP2020 motion controller via a Prologix GPIB to Ethernet adapter

## Installation:

You will need somehow to install Nelsond's repo for the prologix controller (https://github.com/nelsond/prologix-gpib-ethernet). 

With internet access:
```
pip install -e .
```

Without internet access: get a local copy of the repository first, pip install it, and then proceed to installing this package.

## Example usage: 

See the tests folder.