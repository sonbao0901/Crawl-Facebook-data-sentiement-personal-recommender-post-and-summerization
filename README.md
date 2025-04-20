# Facebook Data Analysis and Recommender System

This project provides tools for crawling Facebook data, performing sentiment analysis, and creating a personalized recommender system.

## Project Structure

```
project/
├── data/           # Data storage
│   ├── raw/        # Raw data files
│   ├── processed/  # Processed data files
│   └── resources/  # Resource files (e.g., stopwords)
├── src/            # Source code
│   ├── crawler/    # Facebook data crawler
│   ├── sentiment/  # Sentiment analysis
│   ├── recommender/# Recommender system
│   └── utils/      # Utility functions
├── notebooks/      # Jupyter notebooks
├── config/         # Configuration files
└── requirements.txt# Project dependencies
```

## Features

- Facebook data crawling
- Sentiment analysis for posts and comments
- Personalized recommender system
- Data preprocessing and analysis
- Vietnamese language support

## Requirements

- Python 3.x
- Required packages (see requirements.txt)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Configure your Facebook cookies in `config/cookies.json`
2. Run the Jupyter notebook in `notebooks/` for the complete workflow
3. Or use individual modules from the `src/` directory

## Data Files

- `Theanh28.xlsx`: Raw Facebook data
- `comments.xlsx`: Comment data
- `result_post_sentiment.xlsx`: Sentiment analysis results for posts
- `result_comment_sentiment.xlsx`: Sentiment analysis results for comments
- `vietnamese-stopwords.txt`: Vietnamese stopwords for text processing

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License. 