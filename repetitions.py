import collections
data = open('data.txt', 'r')
sentence = data.read()
words = sentence.split()
word_counts = collections.Counter(words)
unused_words = ["but", "and", "for", "in", "that", "they", "a", "all", "about", "could", "by", "be", "been", "from", "had", "an", "as", "is", "it", "its", "just", "the", "at", "what", "are", "of", "on", "put", "than", "their", "those", "though", "to", "was", "up", "were", "what", "when", "which", "who", "will", "with", "another", "has", "have", "may", "such"]
for word, count in sorted(word_counts.items()):
    if count > 1:
        if word.lower() not in unused_words:
            print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
