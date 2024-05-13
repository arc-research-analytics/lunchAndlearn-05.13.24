# Lunch & Learn // 05.13.24

### Overview

Today's lunch & learn is a demonstration of a possible Python-based worflow from raw data to web application. This repo contains the data and Python scripts to generate a web-based [Streamlit](https://streamlit.io/) web app to visualize home sale prices in Fulton County from 2018 to 2023. The Python scripts and CSVs used in the demonstration are in the "Primary" folder.

Streamlit is a Python-only web framework with out-of-the-box UI elements, while [Plotly/Mapbox](https://plotly.com/python/mapbox-county-choropleth/) will generate the choropleth map.

### Prerequisites

- **Python:** If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/) or consider using a Python distribution like [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html).
- **Visual Studio Code:** While any integrated development environment will work, [VSCode](https://code.visualstudio.com/) is free to download and has become the gold standard in software development across many disciplines.

### Environment

While not strictly necessary, we recommend creating a virtual environment to isolate the dependencies necessary to run this demo. The easiest way to get started is to download a zipped file of the repo contents.

For more advanced users, set up a virtual environment using the `requirements.txt` file in the "Misc" folder before cloning.

### Running the app

Once you have the files, you will need to open the Python file in an IDE of your choice, uncomment the code sections, and start up a local Streamlit server by running `streamlit run StreamlitDemo.py` from a terminal.
