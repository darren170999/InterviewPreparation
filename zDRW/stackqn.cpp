#include<bits/stdc++.h>
using namespace std;

void solve2(){
string s;
cin>>s;
map<char,int> mp;
for(auto x: s){
mp[x]++;
}
vector v;
for(auto x: mp){
if(x.second%2==0){
v.push_back(x.first);
}
}
for(auto x: v){
mp.erase(x);
}
stack st;
for(auto x: s){
if(mp.find(x)==mp.end())continue;
if(!st.empty() and st.top()>=x and mp[st.top()]>0){
st.pop();

    }
    mp[x]--;
    st.push(x);
}
string ans="";
int n=mp.size();
while(!st.empty()){
    ans+=st.top();
    st.pop();
}
reverse(ans.begin(),ans.end());
//only unique elements from it
set<char> st2;
string ans2="";
for(auto x: ans){
    if(st2.find(x)==st2.end()){
        ans2+=x;
        st2.insert(x);

    }
}
cout<<ans2<<endl;
}
int main(){
solve2();
}