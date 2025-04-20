import os
import shutil

def create_directory_structure():
    # Create main directories
    directories = [
        'data/raw',
        'data/processed',
        'data/resources',
        'src/crawler',
        'src/sentiment',
        'src/recommender',
        'src/utils',
        'notebooks',
        'config'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def move_files():
    # Move data files
    shutil.move('Theanh28.xlsx', 'data/raw/')
    shutil.move('Theanh28.npy', 'data/raw/')
    shutil.move('comments.xlsx', 'data/raw/')
    
    # Move processed files
    shutil.move('result_post_sentiment.xlsx', 'data/processed/')
    shutil.move('result_comment_sentiment.xlsx', 'data/processed/')
    
    # Move resources
    shutil.move('vietnamese-stopwords.txt', 'data/resources/')
    
    # Move notebook
    shutil.move('Crawldata_Facebook_Sentiment_RecommenderSystem_Summerization.ipynb', 'notebooks/')
    
    # Move config
    shutil.move('cookies.json', 'config/')

if __name__ == "__main__":
    create_directory_structure()
    move_files()
    print("Project structure has been created and files have been moved successfully!") 