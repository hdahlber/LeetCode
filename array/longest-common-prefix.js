/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let length = strs.length;

    if(length===0){
        return ""
    }
    if(length===1){
        return strs[0];
    }
    strs.sort();

    let end = Math.min(strs[0].length, strs[length-1].length);

    let i = 0;
        while (i < end && strs[0][i] == strs[length-1][i] )
            i++;
   
        let pre = strs[0].substring(0, i);
        return pre;


};