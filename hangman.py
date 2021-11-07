# ### HANGMAN GAME
images= ["\n-___-\n|    \n|    \n|    \n|    \n====",
		 "\n-___-\n|   ¦\n|    \n|    \n|    \n====",
		 "\n-___-\n|   ¦\n|   o\n|    \n|    \n====",
		 "\n-___-\n|   ¦\n|   o\n|   |\n|    \n====",
         "\n-___-\n|   ¦\n|   o\n|  /|\n|    \n====",
		 "\n-___-\n|   ¦\n|   o\n|  /|\ \n|    \n====",
		 "\n-___-\n|   ¦\n|   o\n|  /|\ \n|  /\n|    \n====",
         "\n-___-\n|   ¦\n|   o\n|  /|\ \n|  / \ \n|    \n===="]
print('\n !!!!!! (: HANGMAN GAME :) !!!!!!\n')
hangman_words={"NEWZEALAND","STRAWBERRY","SOFTWAREENGINEER","BADMINTON","BIRYANI"}
word=hangman_words.pop()
letters_of_word=list(word)
inp_letters=list(" "*len(letters_of_word))
print('WORD OF A NAME CONTAINING',len(letters_of_word),'LETTERS\n')
img_count=0
while img_count<len(images):
    user_input=input('Enter a letter:-')
    ind=0
    if user_input in letters_of_word and user_input not in inp_letters:
        for letter in letters_of_word:
            if letter==user_input:
                inp_letters[ind]=letter
            ind+=1
        print(' '.join(inp_letters))
        if letters_of_word==inp_letters:
            print('\nYOU WON THE GAME')
            break
    else:
        print('\t',images[img_count])
        img_count+=1
else:
    print('\nYOU ARE HANGED ','\n==>THE CORRECT WORD IS ',word,'\n')

    
