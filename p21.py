def filter_long_words(words, n):
  long_words = []
  for word in words:
    if len(word) > n:
      long_words.append(word)
  return long_words
