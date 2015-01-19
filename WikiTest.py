import wikipedia
import sys
reload(sys)
LandInfo = wikipedia.summary("Taj Mahal", sentences = 2)
sys.setdefaultencoding('utf-8')
print LandInfo