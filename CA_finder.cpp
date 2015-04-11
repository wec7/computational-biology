#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string* splt(string s, char c) {
    int count = 1;
    for (int i = 1; i < s.length(); ++i )
        if (s[i]==c && s[i-1]!=c) ++count;
    string* ans = new string[count];
    count = 0;
    ans[0] = s[0];
    for (int i = 1; i < s.length(); ++i )
        if (s[i]==c) {if (s[i-1]!=c) ++count;}
        else ans[count] += s[i];
    return ans;       
}

int main() {
    string s, name;
    char *c;
    cin >> s;
    name = splt(s,'.')[0]+".pdb";
    cout << name;
    ifstream fin(s.c_str());
    ofstream fout(name.c_str());
    while (getline(fin, s)) {
       if (s[0]=='E') break;
       string* a = splt(s, ' ');  
       if (a[2]=="CA") 
          fout << a[5] << " " << a[6] << " " << a[7] << endl;
    }
    fin.close();    
}
