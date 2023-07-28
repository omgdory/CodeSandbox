#include <stack>
#include <string>

int main() {
    std::stack<std::string> myStack;

    myStack.push("Gavin");
    myStack.push("Grogg");
    myStack.push("Test");

    myStack.pop();

    return 0;
}
