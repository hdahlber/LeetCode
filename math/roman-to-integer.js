/**
 * @param {string} s
 * @return {number}
 */
 const romanNumerals = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
};
var romanToInt = function(romanNumeral) {
    let decimalNumber = 0;

for (let i = 0; i < romanNumeral.length; i++) {
  const currentSymbol = romanNumeral[i];
  const currentValue = romanNumerals[currentSymbol];
  const nextSymbol = romanNumeral[i + 1];
  const nextValue = romanNumerals[nextSymbol];
  
  if (nextValue && nextValue > currentValue) {
    decimalNumber += (nextValue - currentValue);
    i++;
  } else {
    decimalNumber += currentValue;
  }
}
return decimalNumber

    
};