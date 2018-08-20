import Normalizer.Normalizer_Trash_removal as normalizer
import Ranking.rank as rank

from tkinter import filedialog


#normaliza

inputPath = filedialog.askopenfilename()
data_json = open(inputPath).read()

info = normalizer.normalization(data_json)
info = normalizer.stripNonAlphaNum(info)
info_tokenized = normalizer.tokenize_info(info)

#rankeia e plota
distToPlot =  {}
distToPlot = rank.freqDist(info_tokenized)

distToPlot.plot(20)

