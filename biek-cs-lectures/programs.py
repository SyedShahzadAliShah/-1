"""Complete C++ programs for the BIEK Computer Science lectures.

Directives in the leading comments are read by the test runner:
  // CASE: stdin for one run
  // STDIN: extra stdin line (used when there is no CASE)
  // EXPECT: text that must appear in stdout
"""

PROGRAMS = {}

PROGRAMS["calculator"] = r"""
// CASE: 12 3
// EXPECT: Sum = 15
// EXPECT: Difference = 9
// EXPECT: Product = 36
// EXPECT: Quotient = 4
// CASE: 12 0
// EXPECT: Cannot divide by zero
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;
    cout << "Sum = " << a + b << endl;
    cout << "Difference = " << a - b << endl;
    cout << "Product = " << a * b << endl;
    if (b != 0)
        cout << "Quotient = " << a / b << endl;
    else
        cout << "Cannot divide by zero" << endl;
    return 0;
}
"""

PROGRAMS["marksheet"] = r"""
// CASE: 76
// EXPECT: Grade: B
// CASE: 40
// EXPECT: Grade: Fail
// CASE: 110
// EXPECT: Grade: Invalid
#include <iostream>
using namespace std;

int main() {
    int marks;
    cout << "Enter marks out of 100: ";
    cin >> marks;
    cout << "Grade: ";
    if (marks < 0 || marks > 100)
        cout << "Invalid" << endl;
    else if (marks >= 80)
        cout << "A" << endl;
    else if (marks >= 70)
        cout << "B" << endl;
    else if (marks >= 60)
        cout << "C" << endl;
    else if (marks >= 50)
        cout << "D" << endl;
    else
        cout << "Fail" << endl;
    return 0;
}
"""

PROGRAMS["largest3"] = r"""
// STDIN: 12 40 9
// EXPECT: Largest = 40
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Enter three integers: ";
    cin >> a >> b >> c;
    int largest = a;
    if (b > largest)
        largest = b;
    if (c > largest)
        largest = c;
    cout << "Largest = " << largest << endl;
    return 0;
}
"""

PROGRAMS["weekday"] = r"""
// CASE: 3
// EXPECT: Wednesday
// CASE: 9
// EXPECT: Invalid day
#include <iostream>
using namespace std;

int main() {
    int day;
    cout << "Enter a day number (1 to 7): ";
    cin >> day;
    switch (day) {
        case 1: cout << "Monday" << endl; break;
        case 2: cout << "Tuesday" << endl; break;
        case 3: cout << "Wednesday" << endl; break;
        case 4: cout << "Thursday" << endl; break;
        case 5: cout << "Friday" << endl; break;
        case 6: cout << "Saturday" << endl; break;
        case 7: cout << "Sunday" << endl; break;
        default: cout << "Invalid day" << endl;
    }
    return 0;
}
"""

PROGRAMS["prime"] = r"""
// CASE: 17
// EXPECT: 17 is prime
// CASE: 1
// EXPECT: 1 is neither prime nor composite
// CASE: 18
// EXPECT: 18 is composite
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    if (n <= 1) {
        cout << n << " is neither prime nor composite" << endl;
        return 0;
    }
    bool isPrime = true;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
        cout << n << " is prime" << endl;
    else
        cout << n << " is composite" << endl;
    return 0;
}
"""

PROGRAMS["digits"] = r"""
// CASE: 2024
// EXPECT: 2
// EXPECT: 0
// EXPECT: 2
// EXPECT: 4
// CASE: 85
// EXPECT: Enter a four-digit number
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a four-digit number: ";
    cin >> n;
    if (n < 1000 || n > 9999) {
        cout << "Enter a four-digit number" << endl;
        return 0;
    }
    cout << n / 1000 << endl;
    cout << (n / 100) % 10 << endl;
    cout << (n / 10) % 10 << endl;
    cout << n % 10 << endl;
    return 0;
}
"""

PROGRAMS["factors"] = r"""
// STDIN: 12
// EXPECT: 1 2 3 4 6 12
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    cout << "Factors: ";
    for (int i = 1; i <= n; i++) {
        if (n % i == 0)
            cout << i << " ";
    }
    cout << endl;
    return 0;
}
"""

PROGRAMS["menu_do_while"] = r"""
// STDIN: 1
// STDIN: 4
// STDIN: 0
// EXPECT: Square = 16
// EXPECT: Done
#include <iostream>
using namespace std;

int main() {
    int choice, n;
    do {
        cout << "1. Square a number" << endl;
        cout << "0. Exit" << endl;
        cout << "Choice: ";
        cin >> choice;
        if (choice == 1) {
            cout << "Number: ";
            cin >> n;
            cout << "Square = " << n * n << endl;
        }
    } while (choice != 0);
    cout << "Done" << endl;
    return 0;
}
"""

PROGRAMS["jumps"] = r"""
// EXPECT: 1 2 4 5
// EXPECT: Stopped at 3
#include <iostream>
using namespace std;

int main() {
    cout << "continue skips 3: ";
    for (int i = 1; i <= 5; i++) {
        if (i == 3)
            continue;
        cout << i << " ";
    }
    cout << endl;
    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            cout << "Stopped at 3" << endl;
            break;
        }
    }
    int n = 1;
print_line:
    if (n == 1)
        cout << "goto reached the label" << endl;
    return 0;
}
"""

PROGRAMS["stars"] = r"""
// STDIN: 4
// EXPECT: *
// EXPECT: **
// EXPECT: ***
// EXPECT: ****
#include <iostream>
using namespace std;

void drawStars(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++)
            cout << "*";
        cout << endl;
    }
}

int main() {
    int size;
    cout << "Enter size: ";
    cin >> size;
    drawStars(size);
    return 0;
}
"""

PROGRAMS["larger"] = r"""
// STDIN: 14 22
// EXPECT: Larger = 22
#include <iostream>
using namespace std;

int larger(int a, int b) {
    if (a > b)
        return a;
    return b;
}

int main() {
    int x, y;
    cout << "Enter two integers: ";
    cin >> x >> y;
    cout << "Larger = " << larger(x, y) << endl;
    return 0;
}
"""

PROGRAMS["pass_modes"] = r"""
// EXPECT: After by value: 10
// EXPECT: After by reference: 99
// EXPECT: add(5) = 15
// EXPECT: add(5, 3) = 8
#include <iostream>
using namespace std;

void byValue(int n) { n = 99; }

void byReference(int &n) { n = 99; }

void showConst(const int n) { cout << "Constant parameter: " << n << endl; }

inline int square(int n) { return n * n; }

int add(int a, int b = 10) { return a + b; }

int main() {
    int a = 10;
    byValue(a);
    cout << "After by value: " << a << endl;
    byReference(a);
    cout << "After by reference: " << a << endl;
    showConst(7);
    cout << "square(6) = " << square(6) << endl;
    cout << "add(5) = " << add(5) << endl;
    cout << "add(5, 3) = " << add(5, 3) << endl;
    return 0;
}
"""

PROGRAMS["overload"] = r"""
// EXPECT: int sum = 7
// EXPECT: three sum = 12
// EXPECT: double sum = 5.5
#include <iostream>
using namespace std;

int sum(int a, int b) { return a + b; }

int sum(int a, int b, int c) { return a + b + c; }

double sum(double a, double b) { return a + b; }

int main() {
    cout << "int sum = " << sum(3, 4) << endl;
    cout << "three sum = " << sum(3, 4, 5) << endl;
    cout << "double sum = " << sum(2.5, 3.0) << endl;
    return 0;
}
"""

PROGRAMS["scope_exit"] = r"""
// STDIN: -1
// EXPECT: Goodbye
#include <iostream>
#include <cstdlib>
using namespace std;

int visits = 0;

void leave() {
    cout << "Goodbye" << endl;
    exit(0);
}

int main() {
    int n;
    static int calls = 0;
    calls++;
    visits++;
    cout << "Enter a positive mark, or -1 to stop: ";
    cin >> n;
    if (n < 0)
        leave();
    cout << "Mark stored. calls = " << calls << endl;
    cout << "visits = " << visits << endl;
    return 0;
}
"""

PROGRAMS["array_basics"] = r"""
// EXPECT: Element at index 2 = 30
// EXPECT: Bytes = 20
// EXPECT: Elements = 5
#include <iostream>
using namespace std;

int main() {
    int marks[5] = {10, 20, 30, 40, 50};
    cout << "Element at index 2 = " << marks[2] << endl;
    cout << "Bytes = " << sizeof(marks) << endl;
    cout << "Elements = " << sizeof(marks) / sizeof(marks[0]) << endl;
    cout << "Traverse: ";
    for (int i = 0; i < 5; i++)
        cout << marks[i] << " ";
    cout << endl;
    return 0;
}
"""

PROGRAMS["array_2d"] = r"""
// EXPECT: 1 2 3
// EXPECT: 4 5 6
#include <iostream>
using namespace std;

int main() {
    int table[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int r = 0; r < 2; r++) {
        for (int c = 0; c < 3; c++)
            cout << table[r][c] << " ";
        cout << endl;
    }
    cout << "Row 1, column 2 = " << table[1][2] << endl;
    return 0;
}
"""

PROGRAMS["sort_search"] = r"""
// STDIN: 4
// EXPECT: Sorted: 1 2 4 5
// EXPECT: Names: Ali Hina Sara
// EXPECT: Found at index 2
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int a[] = {5, 1, 4, 2};
    int n = 4;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    cout << "Sorted: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;

    char names[3][10] = {"Sara", "Ali", "Hina"};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2 - i; j++) {
            if (strcmp(names[j], names[j + 1]) > 0) {
                char temp[10];
                strcpy(temp, names[j]);
                strcpy(names[j], names[j + 1]);
                strcpy(names[j + 1], temp);
            }
        }
    }
    cout << "Names: ";
    for (int i = 0; i < 3; i++)
        cout << names[i] << " ";
    cout << endl;

    int key;
    cout << "Search for: ";
    cin >> key;
    int index = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] == key)
            index = i;
    }
    if (index >= 0)
        cout << "Found at index " << index << endl;
    else
        cout << "Not found" << endl;
    return 0;
}
"""

PROGRAMS["average"] = r"""
// STDIN: 4 10 20 30 40
// EXPECT: Average = 25
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "How many numbers? ";
    cin >> n;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        sum += value;
    }
    cout << "Average = " << sum / n << endl;
    return 0;
}
"""

PROGRAMS["matrix"] = r"""
// EXPECT: Sum row0: 2 2 3
// EXPECT: Product row0: 1 2 3
// EXPECT: Product row2: 7 8 9
#include <iostream>
using namespace std;

int main() {
    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int b[3][3] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    int sum[3][3], product[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            sum[i][j] = a[i][j] + b[i][j];
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            product[i][j] = 0;
            for (int k = 0; k < 3; k++)
                product[i][j] += a[i][k] * b[k][j];
        }
    }
    cout << "Sum row0: " << sum[0][0] << " " << sum[0][1]
         << " " << sum[0][2] << endl;
    cout << "Product row0: " << product[0][0] << " "
         << product[0][1] << " " << product[0][2] << endl;
    cout << "Product row2: " << product[2][0] << " "
         << product[2][1] << " " << product[2][2] << endl;
    return 0;
}
"""

PROGRAMS["strings"] = r"""
// STDIN: Ayesha
// EXPECT: Length = 6
// EXPECT: Reverse = ahseyA
// EXPECT: Joined = BIEK Karachi
// EXPECT: Part = Com
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main() {
    char name[40];
    cout << "Enter a single-word name: ";
    cin >> name;
    cout << "Length = " << strlen(name) << endl;
    cout << "Reverse = ";
    for (int i = strlen(name) - 1; i >= 0; i--)
        cout << name[i];
    cout << endl;

    char first[20] = "BIEK";
    char second[20] = "Karachi";
    char joined[40];
    strcpy(joined, first);
    strcat(joined, " ");
    strcat(joined, second);
    cout << "Joined = " << joined << endl;
    if (strcmp(first, second) < 0)
        cout << "BIEK comes before Karachi" << endl;

    string word = "Computer";
    cout << "Part = " << word.substr(0, 3) << endl;
    return 0;
}
"""

PROGRAMS["employee"] = r"""
// STDIN: Ali Teacher 55000
// EXPECT: Name: Ali
// EXPECT: Designation: Teacher
// EXPECT: Salary: 55000
#include <iostream>
#include <cstring>
using namespace std;

struct Employee {
    char name[30];
    char designation[20];
    int salary;
};

int main() {
    Employee emp;
    cout << "Enter name, designation and salary: ";
    cin >> emp.name >> emp.designation >> emp.salary;
    cout << "Name: " << emp.name << endl;
    cout << "Designation: " << emp.designation << endl;
    cout << "Salary: " << emp.salary << endl;
    return 0;
}
"""

PROGRAMS["pointer_basic"] = r"""
// EXPECT: Value = 25
// EXPECT: Through pointer = 25
// EXPECT: New value = 40
#include <iostream>
using namespace std;

int main() {
    int marks = 25;
    int *p = &marks;
    cout << "Value = " << marks << endl;
    cout << "Address stored in p = " << p << endl;
    cout << "Through pointer = " << *p << endl;
    *p = 40;
    cout << "New value = " << marks << endl;
    return 0;
}
"""

PROGRAMS["pointer_double"] = r"""
// STDIN: 4 7
// EXPECT: First = 8
// EXPECT: Second = 14
#include <iostream>
using namespace std;

void doubleBoth(int *a, int *b) {
    *a = *a * 2;
    *b = *b * 2;
}

int main() {
    int first, second;
    cout << "Enter two integers: ";
    cin >> first >> second;
    doubleBoth(&first, &second);
    cout << "First = " << first << endl;
    cout << "Second = " << second << endl;
    return 0;
}
"""

PROGRAMS["student_class"] = r"""
// STDIN: 17 88
// EXPECT: Age: 17
// EXPECT: Percentage: 88
#include <iostream>
using namespace std;

class Student {
private:
    int age;
    float percentage;
public:
    void setData(int a, float p) {
        age = a;
        percentage = p;
    }
    void showData() {
        cout << "Age: " << age << endl;
        cout << "Percentage: " << percentage << endl;
    }
};

int main() {
    Student s;
    int age;
    float percentage;
    cout << "Enter age and percentage: ";
    cin >> age >> percentage;
    s.setData(age, percentage);
    s.showData();
    return 0;
}
"""

PROGRAMS["time_class"] = r"""
// STDIN: 2 15 40
// EXPECT: Time = 2:15:40
#include <iostream>
using namespace std;

class Time {
private:
    int hours;
    int minutes;
    int seconds;
public:
    Time() {
        hours = 0;
        minutes = 0;
        seconds = 0;
    }
    Time(int h, int m, int s) {
        hours = h;
        minutes = m;
        seconds = s;
    }
    void show() {
        cout << "Time = " << hours << ":" << minutes
             << ":" << seconds << endl;
    }
};

int main() {
    int h, m, s;
    cout << "Enter hours, minutes and seconds: ";
    cin >> h >> m >> s;
    Time t(h, m, s);
    t.show();
    Time empty;
    empty.show();
    return 0;
}
"""

PROGRAMS["inheritance"] = r"""
// STDIN: Ayesha 17 4521
// EXPECT: Name: Ayesha
// EXPECT: Age: 17
// EXPECT: Roll: 4521
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    string name;
    int age;
public:
    void setBase(string n, int a) {
        name = n;
        age = a;
    }
    void showBase() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class DriveClass : public Base {
private:
    int roll;
public:
    void setDrive(string n, int a, int r) {
        setBase(n, a);
        roll = r;
    }
    void showDrive() {
        showBase();
        cout << "Roll: " << roll << endl;
    }
};

int main() {
    DriveClass student;
    string name;
    int age, roll;
    cout << "Enter name, age and roll: ";
    cin >> name >> age >> roll;
    student.setDrive(name, age, roll);
    student.showDrive();
    return 0;
}
"""

PROGRAMS["poly"] = r"""
// EXPECT: Square = 16
// EXPECT: Rectangle = 20
// EXPECT: Drive show
#include <iostream>
using namespace std;

class Base {
public:
    void area(int side) {
        cout << "Square = " << side * side << endl;
    }
    void area(int length, int width) {
        cout << "Rectangle = " << length * width << endl;
    }
    virtual void show() {
        cout << "Base show" << endl;
    }
};

class Drive : public Base {
public:
    void show() override {
        cout << "Drive show" << endl;
    }
};

int main() {
    Base shape;
    shape.area(4);
    shape.area(4, 5);
    Drive d;
    Base *p = &d;
    p->show();
    return 0;
}
"""

PROGRAMS["text_file"] = r"""
// EXPECT: Read: Ayesha
// EXPECT: Read: 88
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ofstream outFile("student.txt");
    outFile << "Ayesha" << endl;
    outFile << 88 << endl;
    outFile.close();

    ifstream inFile("student.txt");
    string name;
    int marks;
    inFile >> name >> marks;
    cout << "Read: " << name << endl;
    cout << "Read: " << marks << endl;
    inFile.close();
    return 0;
}
"""

PROGRAMS["binary_file"] = r"""
// EXPECT: Name: Ayesha
// EXPECT: Age: 17
// EXPECT: Percentage: 88.5
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

struct Student {
    char name[20];
    int age;
    float percentage;
};

int main() {
    Student s;
    strcpy(s.name, "Ayesha");
    s.age = 17;
    s.percentage = 88.5f;

    ofstream outFile("student.bin", ios::binary);
    outFile.write(reinterpret_cast<char*>(&s), sizeof(s));
    outFile.close();

    Student loaded;
    ifstream inFile("student.bin", ios::binary);
    inFile.read(reinterpret_cast<char*>(&loaded), sizeof(loaded));
    inFile.close();

    cout << "Name: " << loaded.name << endl;
    cout << "Age: " << loaded.age << endl;
    cout << "Percentage: " << loaded.percentage << endl;
    return 0;
}
"""

PROGRAMS["constructor_student"] = r"""
// EXPECT: Age: 17
// EXPECT: Percentage: 91
#include <iostream>
using namespace std;

class Student {
private:
    int age;
    float percentage;
public:
    Student() {
        age = 0;
        percentage = 0;
    }
    Student(int a, float p) {
        age = a;
        percentage = p;
    }
    void showData() {
        cout << "Age: " << age << endl;
        cout << "Percentage: " << percentage << endl;
    }
};

int main() {
    Student s(17, 91);
    s.showData();
    return 0;
}
"""
