#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int tc = 0; tc < T; tc++) {
        int N;
        cin >> N;
        
        set<char> number;
        int k = 1;
        while (number.size() != 10) {
            int num = N * k;
            string temp = to_string(num);
            
            for (char i : temp) {
                if (number.find(i) == number.end()) {
                    number.insert(i);
                }
            }
            k++;
        }
        
        int ans = N * (k - 1);
        cout << "#" << tc + 1 << " " << ans << endl;
    }
    
    return 0;
}