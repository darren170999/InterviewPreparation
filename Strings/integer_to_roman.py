class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        thousandsMap = {
            1: "M", 2:"MM", 3:"MMM"
        }
        hundredsMap = {
            1: "C", 2:"CC", 3:"CCC", 4:"CD",5: "D",
            6: "DC", 7:"DCC", 8:"DCCC", 9: "CM"
        }
        tensMap = {
            1: "X", 2:"XX", 3:"XXX", 4:"XL",5: "L",
            6: "LX", 7:"LXX", 8:"LXXX", 9: "XC"
        }
        onesMap = {
            1: "I", 2:"II", 3:"III", 4:"IV",5: "V",
            6: "VI", 7:"VII", 8:"VIII", 9: "IX"
        }
        tmp = num
        thousand = num - tmp%1000
        num -= thousand
        hundred = num - tmp%100
        num -= hundred
        ten = num - tmp%10
        num -= ten
        one = num - tmp%1
        # print(thousand, hundred, ten, one)
        if thousand!=0:
            ans+= thousandsMap[thousand//1000]
        if hundred!=0:
            ans+=hundredsMap[hundred//100]
        if ten!=0:
            ans+= tensMap[ten//10]
        if one!=0:
            ans+= onesMap[one]
        return ans