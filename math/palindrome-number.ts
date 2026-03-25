function isPalindrome(x: number): boolean {
    let charArray: Array<string> = x.toString().split("");
    return Number(charArray.reverse().join(""))==x
   
};