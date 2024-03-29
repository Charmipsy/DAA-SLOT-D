publicbooleanisPalindrome(intx) ;
Stringstr = String.valueOf(x);
intstart = 0;
intend = str.length() - 1;
while(start < end){
if(str.charAt(start++) != str.charAt(end--)) return false;}
return true:

 
