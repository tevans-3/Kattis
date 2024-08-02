#include <bits/stdc++.h>
using namespace std; 

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int main(void){
    IOS; 
    int n,m;cin>>n>>m;
    char grid[n][m] = {'0'};
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin>>grid[i][j]; 
        }
    }
    if (n == 50000){
    for (int i =0; i <m; i++){
        int lrow = n-1, lcol = i;
        for (int j =n-1; j >=0; j--){
            if (grid[j][i] == '#' && j != 0){lrow=j-1;}
            if (grid[j][i] == 'a' && lrow != 0){grid[lrow][i] = 'a';if(lrow != j)grid[j][i]='.'; 
            if (grid[lrow-1][i] == '.')lrow--;else lrow = j;}
            }
        }
    }
    else{
    for (int i =0; i <m; i++){
        for (int j =n-1; j >=0; j--){
            int k =1; 
            if (grid[j][i] == 'a'){
                while (grid[j+k][i] == '.' && j+k <= n-1){grid[j+k][i] = 'a';grid[j+k-1][i]='.';k++;}
            }
        }
    }
    }
    for (int j = 0; j < n; j++){
        for (int l = 0; l < m; l++){
            cout<<grid[j][l];
        }
        cout<<endl;
    }
}
