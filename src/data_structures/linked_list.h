#ifndef LINKED_LIST_H 
#define LINKED_LIST_H 

#include <string>
//#include "iterator.h"

class Node{
    public:
        void *value;
        Node *next, *previous;
        // Con- and deconstructor
        Node();
        Node(void *value);
        Node(void *value, Node *next, Node *previous);
        ~Node();
};

class LinkedList{
    public:
        // Con- and deconstructor
        LinkedList();
        //LinkedList(DataStructure * ds);
        ~LinkedList();
        // Modifier
        void *insert(size_t index, void *value);
        void *pushFront(void *value);
        void *pushBack(void *value);
        void *remove(size_t index);
        void *popFront();
        void *popBack();
        void clear();
        // Accessor and query methods
        Node *getNode(size_t index);
        void *get(size_t index);
        void *front();
        void *back();
        bool isEmpty();
        size_t getSize();
        std::string toString();
        // Operators
        // =
        // []
        //Iterator
        // Iterator * getIteratorFront();
        // Iterator * getIteratorEnd();

    private:
        size_t size;
        Node *head, *tail;

};

#endif  // LINKED_LIST_H 