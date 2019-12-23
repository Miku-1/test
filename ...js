 function f(string, key) {
     ptext = string.toUpperCase();
     mainArray = Array(key);

     for (i = 0; i < key; i++) {
         mainArray[i] = Array(ptext.length);
         for (s = 0; s < ptext.length; s++) {
             mainArray[i][s] = "";
         }
     }
     j = 0;
     r = 0;
     for (i = 0; i < ptext.length; i++) {
         p = ptext.substr(i, 1);
         mainArray[j][i] = p;
         if (r = 0) {
             j = j + 1;
         }
         else if (r = 1) {
             j = j - 1;
         }
         if (j = key - 1) {
             r = 1;
         }
         else if (j = 0) {
             r = 0;
         }
     }
     for (i = 0; i < mainArray.length; i++) {
         mainArray[i] = mainArray[i].join("");
     }
     ctext = mainArray.join("");
     return ctext;
 }

