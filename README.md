# PXVoid

## Overview
This Python script calculates the time left until void on any pixel game.

## How to Use

1. **Save Script:**
   - Save `voidcalc.py` to your local machine.

2. **Install Python:**
   - Ensure you have the latest version of Python installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install Required Libraries:**
   - Open your terminal and run the following commands to install the necessary libraries:
     ```bash
     pip install requests
     pip install beautifulsoup4
     pip install pytz
     ```
4. **Customize URL:**
   - Open the `voidcalc.py` file in a text editor of your choice.
   - Locate line 10, which defines the `url` variable.
   - Change the value of the `url` variable to the site of your choice. By default, it's set to `https://pxgame.xyz`.
     - Make sure to include `/void` at the end of the URL, as the script assumes this path for void calculations.


5. **Run the Script:**
   - Execute the script using the following command in your terminal:
     ```bash
     python voidcalc.py
     ```

Note: Make sure to replace `python` with `python3` if that's the command for Python 3 on your system.

Feel free to customize and adapt these instructions according to your specific needs.
