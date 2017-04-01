#ifndef SHAKESPEARECLUSTER_HPP
#define SHAKESPEARECLUSTER_HPP

#include <iostream>
#include <vector>

using namespace std;

//Structs
struct wordItem;
struct options;

//Function for displaying menu
void displayMainMenu();
void displayOptionsMenu1();
void displayOptionsMenu2();

//Function to store inputs
int getInput();

//Function for options Menu
options Options(int &num, string &StopWords);

//Funciton for user input
void handleUserInput();

//Function to build word-int vector
std::vector<wordItem> buildWordVector(string play, int num, string StopWords);

//Functor to sort by Count then Word
bool sortCount(const wordItem& lhs, const wordItem& rhs);

//Function to build stopword vector
void getStopWords(string ignoreWordFileName, vector<string>& _vecIgnoreWords);

//Check common words
bool isCommonWord(string word, vector<string>& _vecIgnoreWords);

//Function to print results
void printTopN(std::vector<wordItem> v, int topN);
void printUniquePara(std::vector<wordItem> v, int topN);

//Function to return total non common words
int getTotalNumberNonCommonWords(std::vector<wordItem> wordItemList, int Size);

//Function to compare all plays and return unique list
std::vector<wordItem> compareWordVector(std::vector<wordItem> v1, std::vector<wordItem> v2);

#endif //SHAKESPEARECLUSTER_HPP