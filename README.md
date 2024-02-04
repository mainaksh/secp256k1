**mod337.py**

**all operations are modulus 115792089237316195423570985008687907852837564279074904382605163141518161494337**

this is to understand how the private keys shift in the entire curve


**python mod337.py**

command: 1 / 2

Result: 57896044618658097711785492504343953926418782139537452191302581570759080747169

command: 1 / 3

Result: 77194726158210796949047323339125271901891709519383269588403442094345440996225

command: 1 / 4

Result: 86844066927987146567678238756515930889628173209306178286953872356138621120753

command: 55364563546532 + 7847678356786784656

Result: 7847733721350331188

command: 1 / 57896044618658097711785492504343953926418782139537452191302581570759080747169

Result: 2

command: 456837468576348578346856783467856 / 45349869845679847569874985698798456798456

Result: 102506666281327787879768743485563871146224187014039254378169358112061021750707

command: 1 / 9

Result: 64328938465175664124206102782604393251576424599486057990336201745287867496854

command: 1 / 4

Result: 86844066927987146567678238756515930889628173209306178286953872356138621120753

command: 86844066927987146567678238756515930889628173209306178286953872356138621120753 x 115792089237316195423570985008687907852837564279074904382605163141518161494336

Result: 28948022309329048855892746252171976963209391069768726095651290785379540373584

command: 86844066927987146567678238756515930889628173209306178286953872356138621120753 + 28948022309329048855892746252171976963209391069768726095651290785379540373584

Result: 0

command: 1 - 115792089237316195423570985008687907852837564279074904382605163141518161494336

Result: 2

command: 2 - 979875987879879879897

Result: 115792089237316195423570985008687907852837564279074904381625287153638281614442

command:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**search_in_txt.py**

**search for compressed public keys under any directory in all the text files**

C:\Users\Admin\Desktop\code>**python search_in_txt.py**

Enter the directory path to search into: C:\Users\Admin\Desktop\code

Enter a 66-character string starting with '03' or '02': 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798

----------------------------------------------------------------------------------------------------------------------------------------

**generatepublickeys.py**

**Generate compressed public keys and saves them in a file**

you can adjust the initial key, target key and increment value as per your choice

you can modify the count inside code to get the desired number of keys and also the name of output file

C:\Users\Admin\Desktop\code>**python generatepublickeys.py**

Enter the initial key in hex format: 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798

Enter the target key in hex format: 03d6597d465408e6e11264c116dd98b539740e802dc756d7eb88741696e20dfe7d

Enter the increment value: 87686587678436785678436

----------------------------------------------------------------------------------------------------------------------------------------

**sortascending.py**

this program can sort extremely large files which contains very large numbers (one number each row) and saves the sorted result in a text file

this can handle input files more than 100 GB in size

both input and output are txt files

**python sortascending.py**


---------------------------------------------------------------------------------------------------------------------------------------

**generaterandomnumbers.py**

this program generates random numbers of 77 digits and saves them in a txt file

you can change 77 to whatever number to get the desired number of digits 

iteration controls the number of random numbers to be generated

**python generaterandomnumbers.py**
