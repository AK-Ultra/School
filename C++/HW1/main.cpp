/**********************
Written by: ALLEN KEEF
TA: Yang Li
Assignment: Homework 1
**********************/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;

//Struct for Dynamic Array
struct wordItem
{
    string word;
    int count;
};

//Struct for inFile (remove punctuation)
struct letter_only: ctype<char>
{
    letter_only(): ctype<char>(get_table()) {}

    static ctype_base::mask const* get_table()
    {
        static vector<ctype_base::mask>
            rc(ctype<char>::table_size,ctype_base::space);

        fill(&rc['A'], &rc['z'+1], ctype_base::alpha);
        return &rc[0];
    }
};

//Functor to sort by Count then Word
bool sortCount(const wordItem& lhs, const wordItem& rhs) { return lhs.count > rhs.count;}

/*
* Function name: getStopWords
* Purpose: read stop word list from file and store into vector
* @param ignoreWordFile - filename (the file storing ignore words)
* @param _vecIgnoreWords - store ignore words from the file (pass by reference)
* @return - none
* Note: The number of words is fixed to 50
*/
void getStopWords(char *ignoreWordFileName, vector<string>& _vecIgnoreWords);

/*
* Function name: isCommonWord
* Purpose: to see if a word is a common word
* @param word - a word (which you want to check if it is a common word)
* @param _vecIgnoreWords - the vector type of string storing ignore/common words
* @return - true (if word is a common word), or false (otherwise)
*/
bool isCommonWord(string word, vector<string>& _vecIgnoreWords);

/*
* Function name: printTopN
* Purpose: to print the top N high frequency words
* @param wordItemList - a pointer that points to an array of wordItems
* @param topN - the number of top frequency words to print
* @return none
*/
void printTopN(wordItem wordItemList[], int topN);

int getTotalNumberNonCommonWords(wordItem wordItemList[], int Size);

const int STOPWORD_LIST_SIZE = 50;

/*******************************************************************************
COMMANDS TO RUN PROGRAM VIA TERMINAL

1) cd Dropbox/CSCI2270/HW1
2) g++ main.cpp
3) ./a.out 10 ./resources/HW1-HungerGames_edit.txt ./resources/HW1-stopwords.txt
*******************************************************************************/

int main(int argc, char* argv[])
{
    //Read in stopwords file into vector and restrict size
    vector<string> vecIgnoreWords(0);
    getStopWords(argv[3], vecIgnoreWords);
    vecIgnoreWords.resize(STOPWORD_LIST_SIZE);

    // verify we have the correct # of parameters, else throw error msg & return
    if (argc != 4)
    {
        cout << "Usage: ";
        cout << argv[0] << " <number of words> <filename.txt> <ignorefilename.txt>";
        cout << endl;
        return 0;
    }

    //Variables
    int num = atoi( argv[1]);
    string data;
    int c = 0;
    int arraySize = 100;
    int numberDoubled = 0;

    //Dynamic Array
    wordItem *wordArray = new wordItem[arraySize];

    //Map of words and occurrence int
    map<string, int> wordCount;

    //Stream in file and construct word-int map
    ifstream inFile;
    //inFile.imbue(locale(locale(), new letter_only()));
    inFile.open(argv[2]);

    //Build wordCount Map
    if (inFile.is_open())
    {
        //cout << "Sample file opened successfully" << endl;
        while(inFile >> data)
        {
            if (isCommonWord(data,vecIgnoreWords) == true)
            ;
            else
            {
            ++wordCount[data];
            }
        }
    }
    else
    {
        cout << "Unable to open file" << endl;
    }
    inFile.close();

    //Copy map to Dynamic Array
    for (map<string, int>::iterator it = wordCount.begin(); it != wordCount.end(); ++it)
    {
        wordArray[c].word = it->first;
        wordArray[c].count = it->second;
        c++;
        if (c >= arraySize)
        {
            numberDoubled ++;
            arraySize = arraySize * 2;
            wordItem *tempArray = new wordItem[arraySize];
            for (int i = 0; i < c; i++)
            {
                tempArray[i] = wordArray[i];
            }
            delete [] wordArray;
            wordArray = tempArray;
        }
    }

    //Sort Dynamic Array by Count
    sort(wordArray, wordArray + arraySize, sortCount);

    //Print Block
    printTopN(wordArray,num);
    cout << "#" << endl;
    cout << "Array doubled: " << numberDoubled << endl;
    cout << "#"<<endl;
    cout << "Unique non-common words: " << c <<endl;
    cout << "#" << endl;
    cout << "Total non-common words: ";
    cout << getTotalNumberNonCommonWords(wordArray, arraySize) << endl;

    return 0;
}


/***************
FUNCTIONS BLOCKS
***************/

void getStopWords(char *ignoreWordFileName, vector<string>& _vecIgnoreWords)
{
    string data;
    ifstream inFile;
    inFile.open(ignoreWordFileName);

    if(inFile.is_open())
    {
        //cout << "stopWords file has been opened!" << endl;
        while(inFile >> data)
        {
            _vecIgnoreWords.push_back(data);
        }
        inFile.close();
    }

    return;
}

bool isCommonWord(string word, vector<string>& _vecIgnoreWords)
{
    if (find(_vecIgnoreWords.begin(), _vecIgnoreWords.end(), word) !=_vecIgnoreWords.end())
    return true;
    else
    return 0;
}

void printTopN(wordItem wordItemList[], int topN)
{
    for (int i = 0; i < topN; i++)
    {
        cout << wordItemList[i].count << " - " << wordItemList[i].word << endl;
    }
    return;
}


int getTotalNumberNonCommonWords(wordItem wordItemList[], int Size)
{
    int totalNonCommon = 0;
    for (int i = 0; i < Size; i++)
    {
        totalNonCommon += wordItemList[i].count;
    }
    return totalNonCommon;
}

