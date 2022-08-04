import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

try:
    from most_common_words import MostFrequentWords
except ModuleNotFoundError:
    from app.most_common_words import MostFrequentWords

class CommonWordChartGetter:
    """
    Generates and saves a basic bar chart showing the 20 most common words in the book.
    """

    def __init__(self, common_words):
        self.common_words = common_words

    def get_common_word_chart(self):

        plt.style.use(['dark_background'])

        plt.rc('axes', titlesize=18)     # fontsize of the axes title
        plt.rc('axes', labelsize=14)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=13)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=13)    # fontsize of the tick labels
        plt.rc('legend', fontsize=13)    # legend fontsize
        plt.rc('font', size=13)          # controls default text sizes

        plt.title("The 20 Most Common Words in 'The Great Gatsby'", fontsize = 20)
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.bar(self.common_words.keys(), self.common_words.values(), color='purple', linewidth=2)
        plt.xticks(rotation=-45)
        
        plt.tight_layout()
        plt.savefig('most_common_words.png', bbox_inches='tight', fig=100)