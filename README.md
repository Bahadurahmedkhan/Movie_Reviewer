# Movie Reviewer

A machine learning project for sentiment analysis of movie reviews using Natural Language Processing (NLP) techniques.

## Project Overview

This project implements a sentiment analysis system that can classify movie reviews as positive or negative. It uses various NLP techniques including:

- Text preprocessing (tokenization, lemmatization, stop word removal)
- TF-IDF vectorization
- Machine learning classification (Naive Bayes)
- Confusion matrix analysis and visualization

## Features

- **Text Preprocessing**: Advanced text cleaning with NLTK and spaCy
- **Sentiment Analysis**: Binary classification (positive/negative)
- **Model Evaluation**: Comprehensive metrics and confusion matrix visualization
- **Jupyter Notebook**: Interactive analysis and experimentation

## Files Description

- `main.ipynb`: Main Jupyter notebook with the complete analysis workflow
- `confusion_matrix_analysis.py`: Python script for sentiment analysis and model evaluation
- `Dataset.csv`: Movie reviews dataset (not included in repo due to size)
- `requirements.txt`: Python dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bahadurahmedkhan/Movie_Reviewer.git
cd Movie_Reviewer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

5. Download spaCy model:
```python
import spacy
spacy.cli.download("en_core_web_sm")
```

## Usage

### Running the Jupyter Notebook
```bash
jupyter notebook main.ipynb
```

### Running the Python Script
```bash
python confusion_matrix_analysis.py
```

## Project Structure

```
Movie_Reviewer/
├── main.ipynb                    # Main analysis notebook
├── confusion_matrix_analysis.py  # Sentiment analysis script
├── requirements.txt              # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore file
└── Dataset.csv                  # Movie reviews dataset (not in repo)
```

## Technologies Used

- **Python**: Core programming language
- **NLTK**: Natural Language Processing toolkit
- **spaCy**: Advanced NLP library
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **matplotlib/seaborn**: Data visualization
- **Jupyter**: Interactive development environment

## Model Performance

The sentiment analysis model provides:
- Text preprocessing with lemmatization and stop word removal
- TF-IDF feature extraction
- Naive Bayes classification
- Confusion matrix visualization
- Classification report with precision, recall, and F1-score

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License.

## Author

Bahadur Ahmed Khan 