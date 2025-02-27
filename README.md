# UV & Sun Exposure Tracker  

## Overview  
The **UV & Sun Exposure Tracker** is a Python script that provides real-time **UV radiation levels**, **sunrise and sunset times**, and **safe sun exposure recommendations** based on a user-provided city name.  

This script integrates two APIs:  
- **OpenCage API** – Converts a city name into geographic coordinates (latitude and longitude).  
- **OpenUV API** – Retrieves UV index data, sunrise and sunset times, and safe sun exposure durations based on skin type.  

By using this script, users can make informed decisions about sun exposure, reducing the risk of overexposure to harmful UV radiation.  

---

## Features  
- **Get UV Index Information**  
  - Fetches the current **UV index** for the specified location.  
  - Displays the **maximum expected UV index** for the day along with its expected time.  

- **Sunrise & Sunset Data**  
  - Provides **sunrise** and **sunset** times for the specified location.  
  - Useful for planning outdoor activities based on daylight hours.  

- **Safe Sun Exposure Recommendations**  
  - Calculates safe sun exposure durations based on **skin type** and **UV levels**.  
  - Helps users determine how long they can stay in the sun before potential skin damage.  

- **User-Friendly Output**  
  - Displays information in a clean and formatted way for easy readability.  
  - Handles errors gracefully, ensuring a smooth experience even if API data is unavailable.  

---

## How It Works  
1. The user enters a **city name**.  
2. The script fetches the **latitude and longitude** using the OpenCage API.  
3. The coordinates are used to retrieve **UV data, sun exposure times, and sunrise/sunset data** from the OpenUV API.  
4. The results are displayed in a structured format, showing:  
   - Current and maximum UV index  
   - Sunrise and sunset times  
   - Recommended sun exposure duration for different skin types  

---

## Setup & Usage  

### Prerequisites  
- Python 3.x installed  
- API keys for **OpenCage** and **OpenUV** (free API keys can be obtained by signing up on their respective websites)  

### Installation  
1. Clone this repository or download the script.  
2. Install dependencies:  
   ```sh
   pip install requests
   ```
3. Replace `geocoding_api_key` and `uv_api_key` in the script with your API keys.  

### Running the Script  
Execute the script using:  
```sh
python script.py
```  
Enter the name of the city when prompted, and the script will display the relevant sun exposure information.  

---

## Example Output  
```
================ UV & Sun Exposure Report ================

UV Radiation Information:
  - Current UV Index: 5.3
  - Maximum UV Index Today: 7.8 (Expected at 12:30 PM)

Sunrise & Sunset Information:
  - Sunrise: 06:45 AM
  - Sunset: 07:15 PM

Recommended Safe Sun Exposure Times:
  - Skin Type I: 10 minutes
  - Skin Type II: 15 minutes
  - Skin Type III: 25 minutes
  - Skin Type IV: 35 minutes

==========================================================
```  

---

## Error Handling  
- If the city name is incorrect or not found, the script will inform the user and prompt for another input.  
- If API calls fail due to network issues or API limits, appropriate messages will be displayed instead of crashing.  

---

