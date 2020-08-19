import re

txt = "hell110oo _YyOoUu ___$%##fFFFFFFuCck223432544"

str = re.sub('[^a-z]+','', txt)

print(str)
