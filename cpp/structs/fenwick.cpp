#include <bits/stdc++.h>
using namespace std;
int n, q;
int64_t tree[1000000];


void add(int idx, int64_t val){
    for(; idx <= n; idx += idx & -idx){
        tree[idx] += val;
    }
}

int64_t sum(int idx){
    int64_t res = 0;
    for(; idx > 0; idx -= idx & -idx){
        res += tree[idx];
    }
    return res;
}



int main(){
    cin >> n >> q;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        add(i + 1, x);
    }
    for(int i = 0; i < q; i++){
        int op;
        cin >> op;
        if(op == 1){
            int idx, val;
            cin >> idx >> val;
            add(idx, val);
        }else{
            int idx;
            cin >> idx;
            cout << sum(idx) << endl;
        }
    }
    return 0;
}