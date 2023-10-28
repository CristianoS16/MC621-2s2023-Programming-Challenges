// Use ChatCPT to translate the code from Python to C++
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> compute_lps_array(const string &pattern) {
    int pattern_len = pattern.size();
    vector<int> lps(pattern_len, 0);
    int len = 0;
    int i = 1;

    while (i < pattern_len) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

int kmp_search(const string &sentence, const string &pattern) {
    int sentence_len = sentence.size();
    int pattern_len = pattern.size();
    if (pattern_len > sentence_len) {
        return 0;
    }
    vector<int> lps = compute_lps_array(pattern);
    int found_patterns_count = 0;
    int sentence_idx = 0;
    int pattern_idx = 0;

    while (sentence_idx < sentence_len) {
        if (sentence[sentence_idx] == pattern[pattern_idx]) {
            sentence_idx++;
            pattern_idx++;
        }
        if (pattern_idx == pattern_len) {
            found_patterns_count++;
            pattern_idx = lps[pattern_idx - 1];
        } else if (sentence_idx < sentence_len && sentence[sentence_idx] != pattern[pattern_idx]) {
            if (pattern_idx != 0) {
                pattern_idx = lps[pattern_idx - 1];
            } else {
                sentence_idx++;
            }
        }
    }
    return found_patterns_count;
}

int main() {
    while (true) {
        string input;
        cin >> input;

        if (input == ".") {
            break;
        }

        if (input.empty()) {
            cout << 0 << endl;
        } else {
            cout << kmp_search(input + input, input) - 1 << endl;
        }
    }

    return 0;
}
