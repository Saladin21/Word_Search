from trie import Trie
from termcolor import colored

def readPuzzle(filename):
    puzzle = []
    T = Trie()
    f = open(filename, 'r')
    line = f.readline()
    line = line.replace(" ", "").strip('\n')
    puzzle.append(line)
    for i in range(len(line)-1):
        line = f.readline()
        line = line.replace(" ", "").strip('\n')
        puzzle.append(line)
    words = f.readlines()
    for string in words:
        T.insert(string.strip('\n').upper())
    return (puzzle, T)

def printPuzzle(puzzle, answer):
    for i in range (len(puzzle)):
        for j in range (len(puzzle)):
            if ((i,j) in answer):
                print(colored(puzzle[i][j], 'red'), end=" ")
            else:
                print(puzzle[i][j], end=" ")
        print("")

def wordSearch(filename):
    (puzzle, words) = readPuzzle(filename)
    n = len(puzzle)
    answer = set()
    printPuzzle(puzzle, answer)
    print("")
    for i in range (len(puzzle)):
        for j in range (len(puzzle)):
            if(words.isRootChildren(puzzle[i][j])):
                
                #cek horizontal kiri ke kanan
                string = puzzle[i][j:n]
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i,j+l))
                #cek horizontal kanan kiri
                string = puzzle[i][j::-1]
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i,j-l))

                #cek vertikal atas ke bawah
                string = []
                for k in range(i, n):
                    string += puzzle[k][j]
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i+l,j))

                #cek vertikal bawah ke atas
                string = []
                for k in range(i, -1, -1):
                    string += puzzle[k][j]
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i-l,j))

                #cek diagonal kiri atas ke kanan bawah
                string = []
                k = 0
                while (i+k < n and j+k <n):
                    string += puzzle[i+k][j+k]
                    k+=1
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i+l,j+l))
                    
                #cek diagonal kiri bawah ke kanan atas
                string = []
                k = 0
                while (i-k >= 0 and j+k <n):
                    string += puzzle[i-k][j+k]
                    k+=1
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i-l,j+l))

                #cek diagonal kanan bawah ke kiri atas
                string = []
                k = 0
                while (i-k >= 0 and j-k >= 0):
                    string += puzzle[i-k][j-k]
                    k+=1
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i-l,j-l))

                #cek diagonal kanan atas ke kiri bawah
                string = []
                k = 0
                while (i+k < n and j-k >= 0):
                    string += puzzle[i+k][j-k]
                    k+=1
                if (len(string) >= words.shortestWordLength):
                    length = words.search(string)
                    for l in range(length):
                        answer.add((i+l,j-l))
    printPuzzle(puzzle, answer)

wordSearch("sports.txt")


