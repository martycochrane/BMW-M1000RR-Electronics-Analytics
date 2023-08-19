# BMW M1000RR Electronics Analytics Toolkit

A working repository of tool kits I've built to help me Analyse and work on the 2022 BMW M1000RR Electronics Kit Package

## Bike Details
- 2022 & 2023 BMW M1000RR
- Kit Electronics
- BMW Race Calibration 2022 with ECU Software 038_002 Type5
- Motec Dash & Data Logger into Motec i2 Standard 1.1
- Championship: IDM 2023

![Sandro](/img/sandro.jpg)

## Objective

To be able to visualise what's happening with the bike on track and where to adapt the parameters in the kit electronics to give the desired effect.

Below you can see two examples taken from turn 5 at Redbull Ring. The idea is to visualise the target slip (surface plot) and the actual slip (green line). If the rider feels the bike is sliding too much or two little then it's very easy to see where the adjustments should be made to optimise the rider feeling



|RCK19 Example 1                |RCK19 Example 2                |
|-------------------------------|-------------------------------|
| ![TC1](/img/objectiveTC1.png) | ![TC2](/img/objectiveTC2.png) |

|RCK22 Example 1                |RCK22 Example 2                |
|-------------------------------|-------------------------------|
| ![TC1](/img/example.gif) | ![TC2](/img/objectiveTC22-2.png) |
## Handy Tools

You will need to export your data from i2 in CSV format and manually remove any lines that appear before the column names like below

![CSV](/img/csvExample.png)

### Visualise All TC Maps

In the RCK22 example there is a tool called ALL-MAPS which helps visualise all the different Traction Control Maps ontop of each other that you set in the corresponding excel file

![All Maps](/img/allmaps.png)

### Visualise EB Open Loop vs Closed Loop Interaction

In the Engine Brake Example Folder you will find a simple way to show your chosen engine brake map vs what's happening on the bike. This will be developed a bit further but this is the first step

![Engine Brake](/img/EBExample.png)

### Suspension Histograms

If you don't have a motec Pro License then you can't see suspension histograms in the software. This allows you to export all data as a CSV and visualise it here

|Version 1                                    |
|---------------------------------------------|
| ![Suspension Histogram](/img/histogram.png) |

|Version 2                                       |
|------------------------------------------------|
| ![Suspension Histogram](/img/histogram-v2.png) |
| ![Suspension Histogram](/img/histogram-table.png) |



## How to use
- Checkout desired folder (RCK19 or RCK22)
- Make sure latest version of python3 is installed on the computer
- Open directory in an IDE like VS Code or in a python notebook environment
- Run example python file
- If you get any errors for missing libraries then install those libraries with `pip install`