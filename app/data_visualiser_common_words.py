import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from most_common_words import MostFrequentWords

url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
bc = MostFrequentWords(url_book)
book = bc.common_words()

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
plt.bar(book.keys(), book.values(), color='purple', linewidth=2)

plt.show()

# Traceback (most recent call last):
#   File "c:\Projects\Projects\Personal\book_analysis\book_data_visualisation\app\data_visualiser_common_words.py", line 1, in <module>
#     import matplotlib.pyplot as plt
# ModuleNotFoundError: No module named 'matplotlib'