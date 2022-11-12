with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
# zählt die Wörter im Text
words = file_contents.split()
word_count = 0
word_count += len(words)
#print(word_count)

# zählt die Anzahl der einzelnen Buchstaben im Text
lowercase = file_contents.lower()
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count_letters = {}
for letter in abc:
    count = lowercase.count(letter)
    count_letters[letter] = count

# sortiert Buchstaben der Häufigkeit nach
cl_sorted = []
cl_list = sorted(count_letters.items(), key=lambda kv: kv[1])
for letter in cl_list[::-1]:
    cl_sorted.append(letter)
#print(cl_sorted)



def main():
    print("---Begin report of books/frankenstein.txt---")
    print(f"{word_count} words found in the document")
    for letter in cl_sorted:
        print(f"The {letter[0]} character was found {letter[1]} times")

main()       