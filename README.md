# Lunch & Learn // 05.13.24

### Overview

This repo contains the data and Python scripts to generate a web-based [Streamlit](https://streamlit.io/) web app to visualize home sale prices in Fulton County from 2018 to 2023. The Python scripts and CSVs used in the demonstration are in the "Primary" folder.

Streamlit is a Python-only web framework with out-of-the-box UI elements, while [Plotly/Mapbox](https://plotly.com/python/mapbox-county-choropleth/) will generate the choropleth map.

### Prerequisites

- **Python:** If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/) or consider using a Python distribution like [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html).
- **Visual Studio Code:** While any integrated development environment will work, [VSCode](https://code.visualstudio.com/) is free to download and has become the gold standard in software development across many disciplines.

### Environment

While not strictly necessary, we recommend creating a virtual environment to isolate the dependencies necessary to run this demo. The easiest way to get started is to download a zipped file of the repo contents.

For more advanced users, follow these steps to set up a virtual environment necessary to run the code out of the box:

1. Clone or download a zipped copy of the repository via the "Code" dropdown menu at the top of the repo. If cloning, you can use the following bash command in your terminal or command prompt: `git clone https://github.com/arc-research-analytics/lunchAndlearn-05.13.24.git`
2. Navigate to the repo directory with the following command: `cd lunchAndlearn-05.13.24`.
3. Create & activate a virtual environment. While you can use the built-in `venv` or lightweight module `virtualenv`, we recommend using conda environments for an isolated development space. This requires installation of either the Anaconda or Miniconda distribution as linked above. You can do this by running `conda create my_environment` and then `conda activate my_environment`.
4. Install dependencies with the following command: `pip install -r requirements.txt`.
5. Open the included `StreamlitDemo.py` file within VSCode to get started coding!

### Running the app

Once you have the files, you will need to open the Python file in an IDE of your choice, uncomment the code sections, and start up a local Streamlit server by running `streamlit run StreamlitDemo.py` from a terminal.
