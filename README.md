# Eclipsis
> An AI-Powered Paraphrasing Tool 🤖

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Flask](https://img.shields.io/badge/Framework-Flask-orange.svg)](https://flask.palletsprojects.com/en/2.0.x/)
=============================

A Flask web app I made for fun in an hour or two that lets you generate text with any LLM locally through [Ollama](https://ollama.com/), and rewrite it sentence by sentence to avoid AI Detectors with the help of tools.

**What is this?** 🤔
---------------

This project is a web-based tool that uses AI-powered language generation to help users paraphrase sentences and avoid detection by AI-powered plagiarism detectors. The tool uses any LLM of your choice through Ollama to generate new sentences, and then allows users to rewrite them sentence by sentence to create a unique piece of writing.

**How does it work?** 🤔
------------------

1. Users input a sentence or paragraph into the tool.
2. Use any LLM you like from Ollama, run locally on your device.
3. The user can then rewrite the generated sentence or paragraph sentence by sentence to create a unique piece of writing.
4. The tool provides a side-by-side comparison of the original sentence and the rewritten sentence, allowing users to easily compare and refine their work.

Why? It's an easy way to generate a piece of writing with AI and then write it in your own words, allowing you to decide if you want to rephrase anything, keep it the same, etc. It also let's you evade AI detectors such as GPTZero confidently.

**Setup** 🛠
------
### Clone the Repository

To get started, clone this repository to your local machine using Git:

```markdown
git clone https://github.com/SpectrixDev/Eclipsis.git
```

### Install Requirements

Next, install the required dependencies using pip:

```markdown
pip install -r requirements.txt
```

### Download Ollama and a model of your choice
Download some models from [Ollama](https://ollama.com/library). Make sure to follow the instructions on the Ollama website for downloading and installing the models. The program should automatically know what models are installed on your machine (tested on Windows)

### Run the Web App

Lastly, run the web app using Python:

```markdown
python app.py
```

This will start the Flask development server, and you can access the web app by navigating to `http://localhost:5000` in your web browser.
		

-----------
**License** 📝
-------

This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing** 🤝
------------

Contributions are welcome! This was rushed for fun. If you'd like to help improve this project, please fork the repo and submit a pull request.
