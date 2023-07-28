template <typename T>
class LinkedList {
    struct node {
        T data;
        node* next;
        node* prev;
    }
    node* portal;

public:
    // constructor
    LinkedList() {
        this->portal = new node();
        portal->next = portal;
        portal->prev = portal;
    }

    // destructor
    ~LinkedList() {
        node* toDelete = portal->next;
        while(toDelete != portal) {
            node* nextup = toDelete->next;
            delete toDelete;
            toDelete = nextup;
        }
        delete portal;
    }

    void LinkedList<T>::headInsert(const T item&){
        node* temp = new node();
        temp->data = item;
        // if empty
        if(portal->next == portal) {
            temp->prev = portal;
            temp->next = portal;
            portal->prev = temp;
            portal->next = temp;
        }
        else {
            // set up temp
            temp->prev = portal;
            temp->next = portal->next;
            // reroute
            portal->next->prev = temp;
            portal->next = temp;
        }
    }

    void LinkedList<T>::tailInsert(const T item&){
        node* temp = new node();
        temp->data = item;
        // if empty
        if(portal->prev == portal) {
            temp->prev = portal;
            temp->next = portal
            portal->prev = temp;
            portal->next = temp;
        }
        else {
            temp->next = portal
            temp->prev = portal->prev;
            portal->prev->next = temp;
            portal->prev = temp;
        }
    }

    void LinkedList<T>::headRemove(){
        if(portal->next = portal)
            return;
        
        // set pointers
        node* toDelete = portal->next;
        portal->next = toDelete->next;
        toDelete->next->prev = portal;
        // set to nulls to be safe
        toDelete->next = nullptr;
        toDelete->prev = nullptr;
        delete toDelete;
    }

    bool LinkedList<T>::isEmpty() {
        return portal->next == portal;
    }


};