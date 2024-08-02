#include <bits/stdc++.h>
using namespace std; 

#include <bits/extc++.h>
using namespace __gnu_pbds; 
typedef tree<string, null_type, less<string>, rb_tree_tag, 
                tree_order_statistics_node_update> ost; 

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

ost tree_male;
ost tree_fmle;

int main(void){
    IOS;
    int cmd; std::string name; int gs;
    std:: string st, end; 
    while (1){
        cin>>cmd;//cout<<"command is:"<<cmd<<"\n";
        if (cmd == 0) break;
        if (cmd == 1){
            cin>>name>>gs; 
            if (gs == 1){
                tree_male.insert(name);
            }
            else{
                tree_fmle.insert(name);
            }
        }
        else if (cmd == 2){
            cin>>name;
            tree_male.erase(name); 
            tree_fmle.erase(name);
        }
        else if (cmd == 3){
            cin>>st>>end>>gs;
            //cout<<st<<end<<gs<<"\n";
            if (gs == 0){
                cout<<(tree_fmle.order_of_key(end)-tree_fmle.order_of_key(st))+(tree_male.order_of_key(end) - tree_male.order_of_key(st))<<"\n";
            }
            if (gs == 1){
                cout<<(tree_male.order_of_key(end) - tree_male.order_of_key(st))<<"\n"; 
            }
            if (gs == 2){
                cout<<(tree_fmle.order_of_key(end)-tree_fmle.order_of_key(st))<<"\n";
            }
        }
        //if (!cmd) break; 
    }
    return 0; 
}
