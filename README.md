# Environment Configuration
````commandline
pip install poetry
poetry install
````
# Project Configuration
- create a folder "output", "scrap_datasets", "scrap_datasets/clean_datasets"
- import datasets to folder "scrap_datasets"
- import .pkl files to folder "output"

# Run the project
## For experimentation
````commandline
jupyter lab
````
1. go to **web_scrapper.ipynb** for web scrapping process. 
2. go to **movie_recommendation.ipynb** for creating the recommendation model

## For running the recommendation system
````commandline
python recommend.py "movie_name" --top_n N
````
##### Example
````commandline
python recommend.py "Shrek" --top_n 5 
````