# local-llama3-sentiment-analysis

This tutorial will guide you through the steps to set up and run a sentiment analysis project using Python. The project includes analyzing comments from a CSV file, sending them to an Ollama API for sentiment analysis, and visualizing the sentiment distribution.

## Prerequisites

- Python 3.10 or higher
- `pip` (Python package installer)
- Ollama API setup and running on `http://localhost:11434`

## Project Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/sentiment-analysis-project.git
cd sentiment-analysis-project
```

### 2. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install all the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Running the Project

You can now run the main script to start the sentiment analysis:

```bash
python3 main.py
```

## Project Structure

- `main.py`: The main script that handles reading comments from a CSV file, sending them to the Ollama API for sentiment analysis, and visualizing the sentiment distribution.
- `requirements.txt`: A file listing all the Python dependencies.


### 5. Preparing the CSV File

Make sure you have a CSV file named `commentsEng.csv` in the same directory as `main.py`. The CSV file should have a column named `commentText` containing the comments to be analyzed.

## Running the Project

After setting up everything, you can run the project using:

```bash
python3 main.py
```

This will analyze the comments from the CSV file, print the comments with their detected sentiments, display a bar chart of the sentiment distribution, and print the CPU usage.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
