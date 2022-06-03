from os import sep
import random


WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    secret_word = random.choice(wordlist)
    return (secret_word)

wordlist = load_words()
secret_word = choose_word(wordlist)

def game(secret_word):
    word_completion = "_" * len(secret_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','y','z','w','x']
    vowel = ['a','e','i','u','o'] 
    usable_letters = vowel + consonant
    tries = 6
    warnings = 3

    print("Adam asmaca oyununa hoşgeldin!\n")
    print(warnings, "uyariniz var.\n")
    print(tries,"tahmin hakkiniz var.")
    print(secret_word)
    print("Kullanabileceğiniz kelimeler:\n")
    print(*usable_letters, sep = ",")
    print("\n",len(secret_word),"uzunluğunda bir kelime düşünüyorum.\n")
    print(word_completion)
    while not guessed and tries > 0:
        guess = input("\nLütfen bir harf ya da kelime tahmin edin: ").lower()
        if guess.isalpha():
            if len(guess) == 1:
                if guess in guessed_letters:
                    if warnings > 0:
                        warnings -=1
                        print("Bu harfi daha önce tahmin ettiniz! Kalan uyariniz: ",warnings)
                    else:
                        tries -= 1
                        print("Bu harfi daha önce tahmin ettiniz. Uyari hakkiniz kalmadiği için tahmin hakkiniz azaldi.\nKalan tahmin hakkiniz",tries)
                elif guess not in secret_word and guess in consonant:
                    guessed_letters.append(guess)
                    tries -= 1
                    usable_letters.remove(guess)
                    print("->",guess, " harfi kelimenin içinde yok.\n-> Kalan tahmin hakkiniz ",tries)
                    print("-> Kullanabileceğiniz harfler: \n")
                    print(*usable_letters, sep= ",")
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    print("\n",word_completion)
                elif guess not in secret_word and guess in vowel:
                    tries -= 2
                    usable_letters.remove(guess)
                    print("->",guess, " harfi kelimenin içinde yok, yanliş ünlü tahmininden dolayi kalan tahmin hakkiniz iki azaldi.")
                    print("-> Kalan tahmin hakkiniz ",tries)
                    print("-> Kullanabileceğiniz harfler: \n")
                    print(*usable_letters, sep= ",")
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    print("\n",word_completion)
                else:
                    guessed_letters.append(guess)
                    print(guess, " harfi kelimenin içinde bulunuyor. İyi tahmin.\n")
                    usable_letters.remove(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    print("\n",word_completion)

                    if "_" not in word_completion:
                        guessed = True
                    else:
                        print("\nKullanabileceğiniz harfler: \n")
                        print(*usable_letters, sep= ",")

            elif guess == secret_word:
                    guessed = True
            else: 
                if guess in guessed_words:
                    if warnings > 0:
                        warnings -= 1
                        print("Bu kelimeyi daha önce denediniz. Kalan uyari hakkiniz ", warnings)
                        print("\nKullanabileceğiniz harfler: \n")
                        print(*usable_letters, sep= ",")
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                        for index in indices:
                           word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        print("\n",word_completion)
                    else:
                        tries -= 1
                        print("Bu kelimeyi daha önce tahmin ettiniz! Uyari hakkiniz kalmadiği için tahmin hakkiniz azalmiştir.\nKalan tahmin hakkiniz ",tries)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        print("\n",word_completion)
                else:
                    guessed_words.append(guess)
                    tries -= 1
                    print("Maalesef kelime " + guess + " değil. Kalan tahmin hakkiniz ", tries)
                    print("\nKullanabileceğiniz harfler: \n")
                    print(*usable_letters, sep= ",")
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    print("\n",word_completion)
        else:
            if warnings > 0:
                warnings -= 1
                print("Lütfen sadece alfabe giriniz! Kalan uyari hakkiniz ", warnings)
            else:
                tries -= 1
                print("Lütfen alfabe giriniz! Uyari hakkiniz kalmadiği için tahmin hakkiniz azalmiştir.\n Kalan tahmin hakkiniz ",tries)
    if guessed:
        print("\nDoğru tahmin ettiniz, tebrikler!")
        word_completion = secret_word
        print("kelimemiz : ",secret_word)
        skor = tries * len(''.join(set(secret_word)))
        print("Bu oyundaki toplam skorunuz: ",skor)
    else:
        word_completion = secret_word
        print("\nTahmin hakkiniz kalmadi, oyunu kaybettiniz.\nKelime :", word_completion)

    
    
if __name__ == "__main__":

    game(secret_word)
