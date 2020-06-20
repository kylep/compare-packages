# compare-packages

Compare the output from two package list to see which packages are different.
I wrote this to help compare working docker images to broken ones.


## Usage

Just pull the repo and run the python scripts with your two files as arguments.

You can change the boolean `SHOW_MATCHING` in either to show all packages even if they
aren't different.

### dpkg

```bash
# export package lists
docker exec <container1> dpkg -l > container1_dpkg
docker exec <container2> dpkg -l > container2_dpkg

# compare them
./compare-dpkg.py container1_dpkg container2_dpkg
```

### pip

```bash
# export packages
docker exec <container1> pip list > container1_pip
docker exec <container2> pip list > container2_pip

# compare them
./compare-pip.py container1_pip container2_pip
```
