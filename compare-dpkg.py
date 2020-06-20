#!/usr/bin/env python3

SHOW_MATCHING=False

import sys

if len(sys.argv) != 3:
    sys.stderr.write("ERROR: Expected 2 args, both paths to dpkg -l output files\n")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]
sys.stdout.write(f"Comparing {file1} to {file2}\n\n")


def parse(filename):
    with open(filename, "r") as fil:
        contents = fil.read().split("\n")
    packages = {}
    for line in contents:
        line_list = [l for l in line.split(" ") if l]
        if not line_list or line_list[0] != "ii":
            continue
        packages[line_list[1]] = line_list[2]
    return packages


left = parse(file1)
right = parse(file2)

packages = list(left)
for package in right:
    if package not in packages:
        packages.append(package)

pad_length = max(30, max(len(file1), len(file2)))+4

# print header
white = "\033[1;37m"
green = "\033[92m"
red = "\033[91m"
endcol = "\033[0m"
arrow = f"{white}>{endcol}".ljust(pad_length+len(white)+len(endcol)-2, " ")
file1_title = f"{green}{file1}{endcol}".ljust(pad_length+len(green)+len(endcol)-2, " ")
file2_title = f"{red}{file2}{endcol}".ljust(pad_length+len(red)+len(endcol)-2, " ")
print(f"{arrow}  {file1_title}  {file2_title}")

# print packages
for package in sorted(packages):
    l_ver = left[package] if package in left else ""
    r_ver = right[package] if package in right else ""
    if l_ver == r_ver and not SHOW_MATCHING:
        continue
    pad_pkg = package.ljust(pad_length, " ")
    pad_l_ver = l_ver[:pad_length].ljust(pad_length, " ")
    pad_r_ver = r_ver[:pad_length].ljust(pad_length, " ")
    print(f"{pad_pkg}{pad_l_ver}{pad_r_ver}")
