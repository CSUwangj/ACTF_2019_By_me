#include <signal.h>
#include <unistd.h>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::rand;
using std::sort;
using std::string;
using std::unique;
using std::vector;

void sigalarm(int sig) {
  cout << endl
       << "ALARM!" << endl;
  exit(0);
}

void init() {
  cout << "Welcome to magic ball challenge~" << endl
       << "There are balls of different amount at each challenge, all identical in appearance," << endl
       << "and all indentical in weight except for one, which is either heavier or lighter than" << endl
       << "the remaining balls. Devise a procedure to identify the counterfeit ball in certain" << endl
       << "amount of weighings with a balance." << endl
       << "BE CAREFUL, it's not a PWN challenge." << endl;
  std::srand(std::time(nullptr));
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  signal(SIGALRM, sigalarm);
  alarm(60);
}

void generate(vector<int> &balls, size_t sz) {
  balls.clear();
  size_t special = rand() % sz;
  // cout << special << endl;
  for (int i = 0; i < sz; ++i) balls.push_back(1);
  balls[special] = (std::time(nullptr) & 1) * 2;
  // cout << balls[special] << endl;
}

int main() {
  init();
  const int rds[3][3] = {{0, 2, 3}, {1, 3, 12}, {2, 7, 1092}};
  const string h = "h", l = "l";
  for (auto &rd : rds) {
    cout << "--------------------------------------------------------------------------------" << endl
         << "Welcome to challenge " << rd[0] << ". In this challenge you have to identify the counterfeit ball" << endl
         << "from " << rd[2] << " balls within " << rd[1] << " weighings." << endl
         << endl
         << "Warning: index out of range or repeated balls is not allowed and it costs one chance." << endl
         << "--------------------------------------------------------------------------------" << endl;
    vector<int> balls;
    generate(balls, rd[2]);
    for (int op = 0; op < rd[1]; ++op) {
      vector<int> left_input, right_input, all_input;
      // cout << left_input.size() << right_input.size() << all_input.size() << endl;
      size_t amount, ball;
      cout << "How many balls do you want to put on left side of the balance?" << endl;
      cin >> amount;
      cout << "Input balls' index(begin at 0, separated by space, \\t or \\n)." << endl;
      for (int i = 0; i < amount; ++i) {
        cin >> ball;
        left_input.push_back(ball);
        all_input.push_back(ball);
      }
      cout << "How many balls do you want to put on right side of the balance?" << endl;
      cin >> amount;
      cout << "Input balls' index(begin at 0, separated by space, \\t or \\n)." << endl;
      for (int i = 0; i < amount; ++i) {
        cin >> ball;
        right_input.push_back(ball);
        all_input.push_back(ball);
      }
      sort(left_input.begin(), left_input.end());
      sort(right_input.begin(), right_input.end());
      sort(all_input.begin(), all_input.end());
      auto end = all_input.end();
      if (end != unique(all_input.begin(), all_input.end())) {
        cout << "Repeated balls appear... Check it." << endl;
        continue;
      }
      if (all_input.back() >= rd[2]) {
        cout << "Overflow index, what are you doing..." << endl;
        continue;
      }
      size_t left_weight = 0, right_weight = 0;
      for (auto b : left_input) left_weight += balls[b];
      for (auto b : right_input) right_weight += balls[b];
      if (left_weight > right_weight)
        cout << "The left side is heavier than the right side" << endl;
      else if (left_weight < right_weight)
        cout << "The right side is heavier than the left side" << endl;
      else
        cout << "As heavy on both sides" << endl;
    }
    size_t ball;
    string result;
    cout << "Which ball is counterfeit?" << endl;
    cin >> ball;
    cout << "It's lighter or heavier? (l for lighter and h for heavier)" << endl;
    cin >> result;
    if (ball >= rd[2] || (result != l && result != h)) {
      cout << "Invalid input." << endl;
      exit(0);
    }
    if ((result == l && balls[ball] != 0) || (result == h && balls[ball] != 2)) {
      cout << "Wrong answer." << endl;
      exit(0);
    }
    cout << "Accept at challenge " << rd[0] << "! WELL DONE!" << endl;
  }
  cout << "AURORA{May_Shannon_be_with_you}" << endl
       << "Hope you enjoy it~" << endl;
}