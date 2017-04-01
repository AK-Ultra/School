#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

struct wordItem
{
    string word;
    int count;
};

struct options
{
	int num;
	string stopwords;
};

bool sortCount(const wordItem& lhs, const wordItem& rhs) 
{ 
	return lhs.count > rhs.count;
}

std::vector<wordItem> compareWordVector(std::vector<wordItem> v1, std::vector<wordItem> v2)
{
	std::vector<wordItem> outputVector;
	for (int i = 0; i < v1.size(); i++)
	{
		int x = 0;
		for (int j = 0; j < v2.size(); j++)
		{
			if (v1[i].word == v2[j].word)
			{
				x = 1;
			}
		}
		if (x == 0)
		{
			outputVector.push_back(v1[i]);
		}
		
	}
	return outputVector;
}

void getStopWords(string ignoreWordFileName, vector<string>& _vecIgnoreWords)
{
    string data;
    ifstream inFile;
    inFile.open(ignoreWordFileName);

    if(inFile.is_open())
    {
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
    return false;
}

void printTopN(std::vector<wordItem> v, int topN)
{	
    cout << "Top " << topN << " Word Occurence:\n" << endl;
    for (int i = 0; i < v.size(); i++)
    {
    	int countSize = v[i].count * 1;
    	cout << countSize << " " << v[i].word << endl;
    }

    cout << "\n";
    return;
}

void printUniquePara(std::vector<wordItem> v, int topN)
{
	cout << "Top unique words in play: \n" << endl;
    for (int i = 0; i < topN; i++)
    {
		cout << v[i].word << " ";
    }
    cout << "\n";
    cout << "\n";
    return;
}

int getTotalNumberNonCommonWords(std::vector<wordItem> v, int Size)
{
    int totalNonCommon = 0;
    for (int i = 0; i < Size; i++)
    {
        totalNonCommon += v[i].count;
    }
    return totalNonCommon;
}

void displayMainMenu()
{
    cout << "====== Main Menu =========\n";
    cout << "Please make your selection\n";
    cout << "1. Richard II\n";
    cout << "2. Julius Caesar\n";
    cout << "3. Antony and Cleopatra\n";
    cout << "4. Options\n";
    cout << "5. Quit\n";
    cout << "Selection: ";
}

void displayOptionsMenu()
{
	cout << "====== Options Menu ======\n";
	cout << "Please make your selection\n";
	cout << "1. Change Word Count\n";
	cout << "2. Change Stopwords\n";
	cout << "3. Back to Main Menu\n";
	cout << "Selection: ";
}

void displayOptionsCount()
{
	cout << "How many top occuring words would you like to display?\n";
	cout << "Selection: ";
}

void displayOptionsStopwords()
{
	cout << "Which stopword list do you want to use?\n";
    cout << "1. Regular\n";
    cout << "2. No Names\n";
    cout << "Selection: ";
}

int getInput()
{
	string choice;
	getline(cin, choice);
	int output = stoi(choice);
	cout << "\n";
	return output;
}

options Options(int &num, string &StopWords)
{	
	bool quit = false;
	int u_input;
	int choice;

	options optionsResults;
	optionsResults.num = num;
	optionsResults.stopwords = StopWords;

	while (!quit)
	{
		displayOptionsMenu();
		choice = getInput();
		switch(choice)
	    {
	    	case 1:
	    	{
	    		displayOptionsCount();
	    		optionsResults.num = getInput();
	    		break;
	    	}

	    	case 2:
	    	{
	    		displayOptionsStopwords();
	    		u_input = getInput();
	    		if (u_input == 1)
			    {
			    	optionsResults.stopwords = "./resources/stopwords.txt";
			    }

			    else if (u_input == 2)
			    {
			    	optionsResults.stopwords = "./resources/stopwordsNonProper.txt";
			    }
		    	break;
		    }

		    case 3:
		    {
		    	quit = true;
		    	break;
		    }

	    	default: 	// invalid input
	        	cout << "Invalid Input" << endl;
	            break;
	    }
	}
	return optionsResults;
}

std::vector<wordItem> buildWordVector(string play, int num, string StopWords)
{
    //Variables
    string data;
    int c = 0;

    //Read in stopwords file into vector
    vector<string> vecIgnoreWords(0);
    getStopWords(StopWords, vecIgnoreWords);

    //Stream in file
    ifstream inFile;
    inFile.open(play);

    //Build wordCount Map
    map<string, int> wordCount;
    if (inFile.is_open())
    {
        //cout << "Sample file opened successfully" << endl;
        while(inFile >> data)
        {
            //Remove Punctuation
            for (int i = 0, len = data.size(); i < len; i++)
            {
                if (ispunct(data[i]))
                {
                    data.erase(i--, 1);
                    len = data.size();
                }
            }
            
            //Make data lowercase
            transform(data.begin(), data.end(), data.begin(), ::tolower);

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

    //Copy map to Vector
    std::vector<wordItem> wordVector(wordCount.size());
    for (map<string, int>::iterator it = wordCount.begin(); it != wordCount.end(); ++it)
    {
        wordVector[c].word = it->first;
        wordVector[c].count = it->second;
        c++;
    }

    //Sort Vector by Count
    sort(wordVector.begin(), wordVector.end(), sortCount);

    //Resize Vector
    wordVector.resize(num);

    return wordVector;
}

void handleUserInput()
{
	bool quit = false;
	string string_input;
	string StopWords = "./resources/stopwords.txt";
	int input;
    int num = 50;

	while (!quit)
	{
	    //Menus
	    displayMainMenu();
	    input = getInput();

	    switch(input)
    	{
	    	case 1:
	    	{
	    		string play = "./resources/richard2.txt";
	    		std::vector<wordItem> v1(num);
	    		std::vector<wordItem> v2(num);
	    		std::vector<wordItem> v3(num);
	    		std::vector<wordItem> unique;
	    		v1 = buildWordVector(play, num, StopWords);
	    		v2 = buildWordVector("./resources/juliusCaesar.txt", num, StopWords);
	    		v3 = buildWordVector("./resources/antonyCleopatra.txt", num, StopWords);
	    		unique = compareWordVector(v1,v2);
	    		unique = compareWordVector(unique,v3);
	    		printTopN(v1,num);
	    		printUniquePara(unique, unique.size());
	    		break;
	    	}

	    	case 2:
	    	{
	    		string play = "./resources/juliusCaesar.txt";
	    		std::vector<wordItem> v1(num);
	    		std::vector<wordItem> v2(num);
	    		std::vector<wordItem> v3(num);
	    		std::vector<wordItem> unique;
	    		v1 = buildWordVector(play, num, StopWords);
	    		v2 = buildWordVector("./resources/richard2.txt", num, StopWords);
	    		v3 = buildWordVector("./resources/antonyCleopatra.txt", num, StopWords);
				unique = compareWordVector(v1,v2);
	    		unique = compareWordVector(unique,v3);
	    		printTopN(v1,num);
	    		printUniquePara(unique, unique.size());
	    		break;
	    	}

	    	case 3:
	    	{
	    		string play = "./resources/antonyCleopatra.txt";
	    		std::vector<wordItem> v1(num);
	    		std::vector<wordItem> v2(num);
	    		std::vector<wordItem> v3(num);
	    		std::vector<wordItem> unique;
	    		v1 = buildWordVector(play, num, StopWords);
	    		v2 = buildWordVector("./resources/richard2.txt", num, StopWords);
	    		v3 = buildWordVector("./resources/juliusCaesar.txt", num, StopWords);
				unique = compareWordVector(v1,v2);
	    		unique = compareWordVector(unique,v3);
	    		printTopN(v1,num);
	    		printUniquePara(unique, unique.size());
	    		break;
	    	}

	    	case 4:
	    	{
	    		options x;
	    		x = Options(num, StopWords);
	    		num = x.num;
	    		StopWords = x.stopwords;
	    		break;
	    	}

	    	case 5:
	    	{
	    		quit = true;
	    		break;
	    	}

	    	default: 	// invalid input
	        	cout << "Invalid Input" << endl;
	            break;
	    }
	}
}
