try:
   S = input("введіть певний текст ")
   word_for_search = input("введіть зарезервовані слова ").lower()
   filter_text = str(S.lower())
   list_words = word_for_search.split()
   print("найдено ", str.upper(word_for_search))

except Exception as e:
   print(e)