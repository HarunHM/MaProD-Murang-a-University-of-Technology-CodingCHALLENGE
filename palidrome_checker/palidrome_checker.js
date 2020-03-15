function checkPalindrom (str) {
      str = str.toLowerCase();
      return str == str.split('').reverse().join('');
    }

    if(checkPalindrom('Racecar')) {
        console.log('Palindrome');
    } else {
        console.log('Not Palindrome');
    }