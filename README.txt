Alliance Plastics 'CornerBoard Calculator'

Source: https://github.com/cheech36/CornerBoardCalculator
Author: Richard Brosius
Company: Alliance Plastics LLC


1) Installation:
This application requires python 2.7.

Packages: python-tk, Pandas

Packages can be installed using pip or anaconda:

Using pip:	
	pip install python-tk
	pip install pandas

Using anaconda:
	conda create -n test_env python=2.7
	conda install pandas

2) Usage:

This application is for internal use at Alliance Plastics to facilitate quick and error free raw material 		calculations.

Valid CornerBoard item codes contain between 7-12 characters in one of the following formats:

i) APCB#
ii) APCB#DX#  

where # refers to a numerical value between 1-4 digits, specifying the legsize, gauge and length of the item.

For example:

i)True Gauge Items:
APCB2212045 -> 2"x2" (Leg size), 120 gauge (thickness), 45" (Length)
APCB15159070 -> 1.5"x1.5" (Leg size), 90 gauge (thickness), 70" (Length)

ii)DX Equivalent Items: 
APCB22120DX45 -> 2"x2" (Leg size), 90 gauge (thickness), 45" (Length)
APCB1515200DX100 -> 1.5"x1.5" (Leg size), 170 gauge(thickness), 100" (Length)



3) Notes:
i) Leg Sizes - Valid leg sizes can have a total length of 3,4,5 or 6 inches total. Where
   the total leg size is leg1 + leg2. For example 2"x2" has a total leg size of 4.

ii) Warehouse - Each warehouse 001 and LVS produces boards of a different density. 
    Thus selecting LVS warehouse applies an adjustment factor to material costs. Warehouse 001 is the default.  

iii) DX items are equivalent to true gauge items less .030

iv) Material weights are output in lbs

4) Example item codes:

- APCB1515200DX43
- APCB1515180120
- APCB22160DX48
- APCB33300DX110
	
