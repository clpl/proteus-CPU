#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

vector<string> terms[3];

inline void lowercase(string &s) {
	int len = (int)s.size();
	for (int i = 0; i < len; i++) {
		s[i] = tolower(s[i]);
	}
}

void init(ifstream &fin) {
	string s;
	int type = 0;
	while (fin >> s) {
		lowercase(s);
		if (s == "default:") type = 0;
		else if (s == "bus_in:") type = 1;
		else if (s == "bus_out:") type = 2;
		else {
			terms[type].push_back(s);
			cout << type << ' ' << s << '\n';
		}
	}
}

int micro_instrs[128];

void add(int &micro_instr, const string &s) {
	int type = -1, pos = -1;
	for (int t = 0; t < 3; t++) {
		int len = (int)terms[t].size();
		for (int i = 0; i < len; i++) {
			if (s == terms[t][i]) {
				type = t, pos = i;
				break;
			}
		}
	}

#define OFFSET0 30
#define OFFSET1 24
#define OFFSET2 16
#define OFFSET3 13
#define OFFSET4 9
#define OFFSET5 6


	if (type == 0) {
		micro_instr |= (1 << (OFFSET1 - pos - 1));

	} else if (type == 1) {
		for (int i = 3; i >= 0; i--) {
			if (pos >> i & 1) {
				micro_instr |= (1 << (OFFSET3 + i));
			}
		}

	} else if (type == 2) {
		for (int i = 4; i >= 0; i--) {
			if (pos >> i & 1) {
				micro_instr |= (1 << (OFFSET4 + i));
			}
		}

	} else if (s == "empty") {
		micro_instr |= (0b1111111 << OFFSET3);

	} else {
		string ss = s.substr(0, 2);
		int len = (int)s.size();
		if (ss == "a:") {
			for (int i = 2; i < len; i++) {
				if (s[i] == '1') {
					micro_instr |= (1 << (OFFSET0 - i + 1));
				}
			}
		} else if (ss == "p:") {
			cout << "p\n";
			for (int i = 2; i < len; i++) {
				if (s[i] == '1') {
					micro_instr |= (1 << (OFFSET4 - i + 1));
				}
			}
		} else if (ss == "n:") {
			cout << "n\n";
			for (int i = 2; i < len; i++) {
				if (s[i] == '1') {
					micro_instr |= (1 << (OFFSET5 - i + 1));
				}
			}
		}
	}

}

void process(ifstream &fin, ofstream &fout) {
	string s;
	bool flag = true;
	int index = -1, micro_instr;
	while (fin >> s) {
		lowercase(s);
		if (s.substr(0, 2) == "//") {
			getline(fin, s);
			fin >> s;
		}
		if (flag) {
			index = 0;
			int len = (int)s.size();
			for (int i = 0; i < len; i++) {
				index <<= 1;
				index |= s[i] == '1';
			}
			flag = false;
			micro_instr = 0;
			cout << "--------------------\n";
			cout << '<' << index << ">\n";
		} else {
			if (s == "end") {
				micro_instrs[index] = micro_instr;
				flag = true;
				index = -1;
				cout << "====================\n";
			} else if (index >= 0) {
				add(micro_instr, s);
				cout << "[" << micro_instr << "]\n";
			}
		}
	}

	for (int i = 0; i < 128; i++) {
		fout << "ADDR ";
		fout.width(4); fout.fill('0');
		fout << std::hex << i << "H\n";
		for (int j = OFFSET0 - 1; j >= 0; j--) {
			if (micro_instrs[i] >> j & 1) fout << '1';
			else fout << '0';
		}
		fout << '\n';
	}
}

int main() {
	ifstream finit("terms.txt");
	if (!finit.is_open()) {
		cerr << "No terminals file !" << endl;
		exit(0);
	}
	init(finit);
	finit.close();

	ifstream fin("input.txt");
	if (!fin.is_open()) {
		cerr << "No input file !" << endl;
		exit(0);
	}

	ofstream fout("output.txt");
	if (!fout.is_open()) {
		cerr << "No output file !" << endl;
		exit(0);
	}

	process(fin, fout);
	fin.close();
	fout.close();

	return 0;
}
