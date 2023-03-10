# Resize_bulk
Algorithm to resize images in bulk using PIL



### Things to consider:
- Using zero padding grants that the image ratio is maintained. Without padding the ratio WILL be changed;


- All images you want to resize must be in folders inside the "datasets" folder;


- Anything except for folders in the "datasets" folder will be ignored without warnings;


- You will get an assertion error if the "datasets" folder is empty.

### Arguments to parse:
-padding: use "padding" if you want resize using zero padding. Anything else will result in resizing without padding (default = "padding"). 

-x: expected image's width (default = 640).

-y: expected image's height (default = 640).

-prefix: prefix string inserted to the resulting image's name (default = "").

### Usage:
I - Clone this repository using `git clone <insert repository URL>`

II - Make sure pip is up-to-date, then install the requirements using `resize_bulk$ pip install - requirements.txt` 


III - Put your dataset in folders inside the "datasets" folder.

IV - run `resize_bulk$ python resize_bulk.py -padding <insert padding> -x <insert expected width> -y <insert expected height>. -prefix <insert prefix>` 

V - The resulting images will be organized inside the "results" folder in folders with the same names of the original ones.

 