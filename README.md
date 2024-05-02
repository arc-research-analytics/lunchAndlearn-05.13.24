# Lunch & Learn // 05.13.24

### Overview

This repo contains the Python file (StreamlitDemo.py) and source data (FultonCountySales.csv) to generate a web-based [Streamlit application](https://streamlit.io/) modeling home sale prices in Fulton County from 2018 to 2023.

Streamlit is a Python-only web framework with out-of-the-box UI elements, while the Python libraries [Pydeck](https://deckgl.readthedocs.io/en/latest/) and [Plotly Express](https://plotly.com/python/plotly-express/) generate the visuals.

### Prerequisites

- **Python:** If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/) or consider using a Python distribution like [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html).
- **Git:** Git is required to clone this repository. You can download and install Git from the [official Git website](https://git-scm.com/downloads).
- **Visual Studio Code:** While any integrated development environment will work, [VSCode](https://code.visualstudio.com/) is free to download and has become the gold standard in software development across many disciplines.

### Environment

While not strictly necessary, we recommend creating a virtual environment to isolate the dependencies necessary to run this demo. Follow these steps to set up the Python environment for the presentation:

1. Clone or download a zipped copy of the repository via the "Code" dropdown menu at the top of the repo. If cloning, you can use the following bash command in your terminal or command prompt: `git clone hthttps://github.com/arc-research-analytics/lunchAndlearn-05.13.24.git`
2. Navigate to the repo directory with the following command: `cd lunchAndlearn-05.13.24`.
3. Create & activate a virtual environment. While you can use the built-in `venv` or lightweight module `virtualenv`, we recommend using conda environments for an isolated development space. This requires installation of either the Anaconda or Miniconda distribution as linked above. You can do this by running `conda create my_environment` and then `conda activate my_environment`.
4. Install dependencies with the following command: `pip install -r requirements.txt`.
5. Open the included `StreamlitDemo.py` file within VSCode to get started coding!
