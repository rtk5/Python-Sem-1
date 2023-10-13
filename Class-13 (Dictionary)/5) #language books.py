#language books

books_data = '''sanskrit kalidasa shakuntala
english r_k_narayan maligudi_days
kannada kuvempu ramayanadarshanam
sanskrit bhasa swapnavasavadatta
english r_k_narayan dateless_diary
kannada kuvempu malegalalli_madumagalu
sanskrit bhasa kadambari'''

#find the number of books
print('no. of books',len(set(books_data.split('\n'))))

#find the number of languages
lang_set=set()
for i in books_data.splitlines():
    lang=i.split()[0]
    #print(lang)
    lang_set.add(lang)
print('Number of language',len(lang_set))

#display the list of books in each language


#find no. of authors in each language


