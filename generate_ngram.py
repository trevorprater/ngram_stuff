from collections import OrderedDict

def generate_ngram(tokens, n):
	ngrams = dict()

	for i in range(len(tokens) - n + 1): 
		if len(tokens) < n:
			return ngrams
		ngram = (tokens[i:i+n])
		print ngram
		try:
			ngrams[ngram] += 1
		except:
			ngrams[ngram] = 0
		#ngrams.append(tuple(tokens[i:i+n])) 
	sorted(ngrams.items(), key=lambda x: x[1])
	return OrderedDict(sorted(ngrams.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
	text = "I am just backing up some random code."
	generate_ngram(text, 7)
