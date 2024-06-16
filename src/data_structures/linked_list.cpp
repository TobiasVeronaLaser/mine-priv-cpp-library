#include "linked_list.h"
#include <iostream>

// #define DO

#ifdef  DO
#define DEBUG() std::cout << "At line:" << __LINE__ << "\n"
#else
#define DEBUG() 
#endif
/**
 * Node (LinkedList)
 */

Node::Node(){
    value = NULL;
    next = NULL;
    previous = NULL;
}
    
Node::Node(void *value){
        this->value = value;
        next = NULL;
        previous = NULL;
}

Node::Node(void *value, Node *next, Node *previous){
        this->value = value;
        this->next = next;
        this->previous = previous;
}

Node::~Node(){

}

/** 
 * LinkedList
 */

// Con- and deconstructor

LinkedList::LinkedList(){
    size = 0;
    head = nullptr;
    tail = nullptr;
}

LinkedList::~LinkedList(){
    // TODO
}

// Modifier

void *LinkedList::insert(size_t index, void *value){
    if(!value){
        DEBUG();
        return nullptr;
    }
    Node *currentNode = getNode(index);
    std::cout << currentNode << "\tp\n";
    if(!currentNode && index != size){
        DEBUG();
        return nullptr;
    }
    Node *newNode = new Node(value, currentNode, currentNode ? currentNode->previous : nullptr);
    if(size && !index){
        DEBUG();
        head->previous = newNode;
    }
    if(!index){
        DEBUG();
        head = newNode;
    }
    if(size && index == size){
        DEBUG();
        newNode->previous = tail;
        tail->next=newNode;
    }
    if(index == size){
        DEBUG();
        tail = newNode;
    }
    if(size && index && index != size){
        DEBUG();
        currentNode->previous->next = newNode;
        currentNode->previous = newNode;
    }
    ++size;
    std::cout << head->value << "\t" << ((tail->previous) ?  tail->previous->value : 0) << "\n";
    return value;
}

void *LinkedList::pushFront(void *value){
    return insert(0, value);
}

void *LinkedList::pushBack(void *value){
    return insert(size, value);
}

void *LinkedList::remove(size_t index){
    Node *currentNode = getNode(index);
    if(!currentNode){
        DEBUG();
        return nullptr;
    }
    return currentNode->value;
}

void *LinkedList::popFront(){
    return remove(0);
}

void *LinkedList::popBack(){
    return remove(size - 1);
}

void LinkedList::clear(){
    // TODO
}

// Accessor and query methods

Node *LinkedList::getNode(size_t index) {
    if(index >= size){
        DEBUG();
        return nullptr;
    }
    Node *currentNode;
    if(index < size / 2){
        DEBUG();
        currentNode = head;
        for(size_t i = 0; i < index; i++){
            currentNode = currentNode->next;
        }
    }else{
        DEBUG();
        currentNode = tail;
        for(size_t i = size - 1; i > index; --i){
            currentNode = currentNode->previous;
        }
    }
    DEBUG();
    return currentNode;
}

void *LinkedList::get(size_t index){
    Node *currentNode = getNode(index);
    if(!currentNode){
        DEBUG();
        return nullptr;
    }
    return currentNode->value;
}

void *LinkedList::front(){
    return get(0);
}

void *LinkedList::back(){
    return get(size - 1);
}

bool LinkedList::isEmpty(){
    return !head && !tail;
}

size_t LinkedList::getSize(){
    return size;
}

std::string LinkedList::toString(){
    return "" + size;
}

// Operators

// =
// []

//Iterator

// Iterator *LinkedList::getIteratorFront();
// Iterator *LinkedList::getIteratorEnd();


int main(void){
    LinkedList ll = LinkedList();
    int values[] = {1,2,3,4};
    size_t len = sizeof(values)/sizeof((*values));
    for(size_t i = 0; i < len; i++){
        ll.pushBack(&values[i]);
    }

    for(size_t i = 0; i < len; i++){
        ll.pushFront(&values[i]);
    }
    std::string text = "Hello World";
    ll.insert(4, &text);


    
    for(size_t i = 0; i < ll.getSize(); i++){
        std::cout << i << ":" << *(int *)(ll.get(i)) << "\n";
    }
    return EXIT_SUCCESS;
}