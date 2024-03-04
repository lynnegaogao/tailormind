## Introducing Iterators

All of the library containers have iterators, but only a few of them support the subscript operator.

```c++
auto b = v.begin(), e = v.end();
```

The iterator returned by end is an iterator positioned “one past the end” of the associated container (or string). If the container is empty, begin returns the same iterator as the one returned by end.

<img src="https://p.ipic.vip/7gzhit.png" alt="Screenshot 2024-03-04 at 3.58.09 PM" style="zoom:50%;" />

```c++
string s("some string");
if (s.begin() != s.end()) {
  auto it = s.begin();
  *it = toupper(*it);
}
```

As with size_type, the library types that have iterators define types named `iterator` and `const_iterator` that represent actual iterator types:

```c++
vector<int>::iterator it; // it can read and write vector<int> elements 
string::iterator it2; // it2 can read and write characters in a string
vector<int>::const_iterator it3; // it3 can read but not write elements
string::const_iterator it4; // it4 can read but not write characters
```