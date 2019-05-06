#include <signal.h>
#include <unistd.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <regex>
#include <set>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::rand;
using std::regex;
using std::regex_match;
using std::string;
using std::swap;
using std::vector;

vector<string> not_match_of_addtion, match_of_addtion, not_match_of_subtraction, match_of_subtraction,
    not_match_of_gcd, match_of_gcd, not_match_of_multiples, match_of_multiples, not_match_of_fibonacci,
    match_of_fibonacci;

enum {
  ROUND1_LENGTH = 20,
  ROUND2_LENGTH = 30,
  ROUND3_LENGTH = 30,
  ROUND4_LENGTH = 150,
  ROUND5_LENGTH = 200,
};

void sigalarm(int sig) {
  cout << endl
       << "ALARM!" << endl;
  exit(0);
}

bool challenge(const regex &input, const vector<string> &match, const vector<string> &not_match) {
  std::smatch tmp;
  vector<string> wrong_not_match;
  vector<string> wrong_match;

  for (auto &m : match) {
    if (!regex_search(m, tmp, input)) wrong_not_match.push_back(m);
  }

  for (auto &m : not_match) {
    if (regex_search(m, tmp, input)) wrong_match.push_back(m);
  }

  if (wrong_not_match.size() || wrong_match.size()) {
    if (wrong_not_match.size()) {
      cout << "You should match these but don't:" << endl;
      for (auto &m : wrong_not_match) {
        cout << m << endl;
      }
      cout << endl;
    }
    if (wrong_match.size()) {
      cout << "You shouldn't match these but do match these:" << endl;
      for (auto &m : wrong_match) {
        cout << m << endl;
      }
      cout << endl;
    }
    cout << "Try again!" << endl;
    return false;
  }
  return true;
}

void print_challenge(int length, const vector<string> &match, const vector<string> &not_match, string hint) {
  cout << "Input a regex within " << length << " chars. Which should" << endl;
  cout << "Match all of following:" << endl;
  for (auto &m : match) {
    cout << m << endl;
  }
  cout << endl
       << "And none of following:" << endl;
  for (auto &m : not_match) {
    cout << m << endl;
  }
  cout << "HINT: " << hint << endl;
}

void generate_subtraction() {
  std::stringstream buffer;
  string s;
  for (int i = 0; i < 20; ++i) {
    int a = rand() % 51 + 1;
    int b = rand() % 51 + 1;
    if (a < b) swap(a, b);
    if (a == b) a += 1;
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << '-';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << '=';
    for (int j = 0; j < a - b; ++j) buffer << 'x';
    buffer >> s;
    match_of_subtraction.push_back(s);
    buffer.clear();
  }

  for (int i = 0; i < 20; ++i) {
    int a = rand() % 51 + 5;
    int b = rand() % 51 + 5;
    int c = rand() % 7 - 4;
    if (c == 0) c = -4;
    if (a < b) swap(a, b);
    a += 7;
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << '-';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << '=';
    for (int j = 0; j < a - b - c; ++j) buffer << 'x';
    buffer >> s;
    not_match_of_subtraction.push_back(s);
    buffer.clear();
  }
}

void generate_addition() {
  std::stringstream buffer;
  string s;
  for (int i = 0; i < 20; ++i) {
    int a = rand() % 23 + 1;
    int b = rand() % 23 + 1;
    int c = rand() % (a + b) + 1;
    int d = a + b - c;
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << '+';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << '=';
    for (int j = 0; j < c; ++j) buffer << 'x';
    buffer << '+';
    for (int j = 0; j < d; ++j) buffer << 'x';
    buffer >> s;
    match_of_addtion.push_back(s);
    buffer.clear();
  }

  for (int i = 0; i < 20; ++i) {
    int a = rand() % 23 + 1;
    int b = rand() % 23 + 1;
    int c = rand() % (a + b - 1) + 1;
    int d = a + b - c;
    int e = rand() % 5 + 1;
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << '+';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << '=';
    for (int j = 0; j < c; ++j) buffer << 'x';
    buffer << '+';
    for (int j = 0; j < d + e; ++j) buffer << 'x';
    buffer >> s;
    not_match_of_addtion.push_back(s);
    buffer.clear();
  }
}

void generate_gcd() {
  std::stringstream buffer;
  string s;
  for (int i = 0; i < 20; ++i) {
    int a = rand() % 107 + 1;
    int b = rand() % 107 + 1;
    buffer << "gcd(";
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << ',';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << ")=";
    for (int j = 0; j < std::__gcd(a, b); ++j) buffer << 'x';
    buffer >> s;
    match_of_gcd.push_back(s);
    buffer.clear();
  }

  for (int i = 0; i < 20; ++i) {
    int a = rand() % 107 + 1;
    int b = rand() % 107 + 1;
    int c = rand() % 7 + 1;
    buffer << "gcd(";
    for (int j = 0; j < a; ++j) buffer << 'x';
    buffer << ',';
    for (int j = 0; j < b; ++j) buffer << 'x';
    buffer << ")=";
    for (int j = 0; j < std::__gcd(a, b) + c; ++j) buffer << 'x';
    buffer >> s;
    cout << a << endl
         << b << endl
         << std::__gcd(a, b) + c << endl;
    not_match_of_gcd.push_back(s);
    buffer.clear();
  }
}

void generate_multiples() {
  std::stringstream buffer;
  string s;

  for (int i = 0; i < 30; ++i) {
    int a = rand() / 3 * 3;
    if (rand() & 1) buffer << '0';
    buffer << a;
    buffer >> s;
    match_of_multiples.push_back(s);
    buffer.clear();
  }

  for (int i = 0; i < 30; ++i) {
    int a;
    do {
      a = rand();
    } while (a % 3 == 0);
    if (rand() & 1) buffer << '0';
    buffer << a;
    buffer >> s;
    not_match_of_multiples.push_back(s);
    buffer.clear();
  }
}

void generate_fibonacci() {
  std::set<int> st;
  std::stringstream buffer;
  string s;
  int a = 1;
  int b = 1;
  for (int i = 0; i < 20; ++i) {
    for (int j = 0; j < a; ++j) buffer << 'x';
    st.insert(a);
    buffer >> s;
    b = a + b;
    a = b - a;
    match_of_fibonacci.push_back(s);
    buffer.clear();
  }

  for (int i = 0; i < 20; ++i) {
    int a;
    do {
      a = rand() % 233 + 1;
    } while (st.count(a));
    for (int j = 0; j < a; ++j) buffer << 'x';
    st.insert(a);
    buffer >> s;
    b = a + b;
    a = b - a;
    not_match_of_fibonacci.push_back(s);
    buffer.clear();
  }
}

void init() {
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  generate_subtraction();
  generate_addition();
  generate_gcd();
  generate_multiples();
  generate_fibonacci();
  signal(SIGALRM, sigalarm);
  alarm(60);
}

int main() {
  cout << "Welcome to advanced regex challenge~" << endl
       << "Complete 5 challenges and I'll give you flag" << endl;
  std::srand(std::time(nullptr));
  sleep(5);

  init();
  string input;
  regex test;

  print_challenge(ROUND1_LENGTH, match_of_subtraction, not_match_of_subtraction, "Subtraction");
  do {
    cout << "Your regex:";
    cin >> input;
    if (input.size() > ROUND1_LENGTH) {
      cout << "Invalid Input!" << endl;
      continue;
    }
    test = regex(input);
  } while (!challenge(test, match_of_subtraction, not_match_of_subtraction));

  print_challenge(ROUND2_LENGTH, match_of_addtion, not_match_of_addtion, "Addition");
  do {
    cout << "Your regex:";
    cin >> input;
    if (input.size() > ROUND2_LENGTH) {
      cout << "Invalid Input!" << endl;
      exit(0);
    }
    test = regex(input);
  } while (!challenge(test, match_of_addtion, not_match_of_addtion));

  print_challenge(ROUND3_LENGTH, match_of_gcd, not_match_of_gcd, "Euclid");
  do {
    cout << "Your regex:";
    cin >> input;
    if (input.size() > ROUND3_LENGTH) {
      cout << "Invalid Input!" << endl;
      exit(0);
    }
    test = regex(input);
  } while (!challenge(test, match_of_gcd, not_match_of_gcd));

  print_challenge(ROUND4_LENGTH, match_of_multiples, not_match_of_multiples, "Multiples");
  do {
    cout << "Your regex:";
    cin >> input;
    if (input.size() > ROUND4_LENGTH) {
      cout << "Invalid Input!" << endl;
      exit(0);
    }
    test = regex(input);
  } while (!challenge(test, match_of_multiples, not_match_of_multiples));

  print_challenge(ROUND5_LENGTH, match_of_fibonacci, not_match_of_fibonacci, "Fibonacci");
  do {
    cout << "Your regex:";
    cin >> input;
    if (input.size() > ROUND5_LENGTH) {
      cout << "Invalid Input!" << endl;
      exit(0);
    }
    test = regex(input);
  } while (!challenge(test, match_of_fibonacci, not_match_of_fibonacci));

  cout << "WOW! You're so powerful!!!" << endl
       << "AURORA{sorry_for_low_CPU}" << endl;
  return 0;
}