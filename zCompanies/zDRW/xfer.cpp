#include<bits/stdc++.h>
using namespace std;
void solve(){
string s;
cin>>s;
int n;
cin>>n;
vector arr(n);
for(int i=0;i<n;i++){
cin>>arr[i];

}
int ansa=0;
int ansb=0;
int cnta=0;
int cntb=0;
for(int i=0;i<n;i++){
    if(s[i]=='A'){
        //b should give money to a  b-arr[i]>=0 if not convert b to arr[i] cost will be arr[i]-b
        if(ansb-arr[i]>=0){
            ansb-=arr[i];

        }
        else{
            cntb+=arr[i]-ansb;
            ansb=0;
        }
        ansa+=arr[i];
    }
    else{
        if(ansa-arr[i]>=0){
            ansa-=arr[i];
        }
        else{
            cnta+=arr[i]-ansa;
            ansa=0;
        }
        ansb+=arr[i];
    }
}
cout<<cnta<<" "<<cntb<<endl;
}
int main(){
solve();
}