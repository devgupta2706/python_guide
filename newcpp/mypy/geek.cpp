#include <iostream>
using namespace std;
struct node
{
    string name;
};
struct graph
{
    string name;
    int value = 0;
    graph *N = new graph[this->value];
};
int main()
{
    graph G;
    return 0;
}
