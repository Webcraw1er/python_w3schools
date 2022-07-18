"""
1. regEx is a "Regular expression" that is a sequence of characters that forms a search pattern.
2. Can be used to check if a string contains the specified search pattern.
3. this is packed in a module package called "re" module.

"""

#1. import the shit.
print("\n1.")
import re
txt= "the rain in Spain"
txt10= "abracadabra"
txt100= "rairaichachacha"
x= re.search("^the.*Spain$", txt)
w= re.search("^the*Spain$", txt)
y= re.search("^the.*Korea$", txt)
z= re.search("^the.", txt)
v= re.search("^the", txt)
s= re.search("^ab.......ra", txt10)
t= re.search("^ab*ra", txt10)
r= re.search("^abrac*ra", txt10)        # -> none
u= re.search("^ab.*ra", txt10)
h= re.search("^abr.*ra$", txt10)
i= re.search("ab{1}ra", txt10)
j= re.search("cha", txt100)
# just look how it turns out. 이 메타캐릭터들로 문법을 짜는 거다.
# 예를 들어 . 하나면, 그냥 "하나의" 아무 캐릭터를 의미.
# 그러나 .* 라면, "어떤 캐릭터가 몇 개 오든간에" 라는 의미가 된다.
# 즉, *, +, ?, {} 는 모두 다른 메타 캐릭터의 뒤에 붙어 그 캐릭터가 오는 개수를 정의한다.
print(x)
print(w)
print(y)
print(z)
print(v)
print(s)
print(t)
print(r)
print(u)
print(h)
print(i)
print(j)
x= re.findall("the", txt)
print(x)


#2. Metacharacters
print("\n2.")
y= re.search("r.{2}n", txt)
if y:
    print("yes, there is ", y, "in the txt")

#3. special sequences
print("\n3.")
txt= "1st thing 2nd and 3rd abbr."
print(re.findall("\d.{2}", txt))
print(re.findall("ab{2}r", txt))  # <-- two b's
print(re.findall("a.{2}r", txt))  # <-- two letters after "a" 

#4. findall()
print("\n4.")
# finds all matches.
txt= "Rain in Spain"
x= re.findall("ai", txt)
y= re.findall("KOrea", txt)
print(x)
print(y)

#5. split
print("\n5.")
txt= "Buy my mama chandeliers on my tears dammit"
print(re.split("\s", txt))
print(re.split("\s", txt, 3))

#6. replace
print("\n6.")
txt="the rain in paris"
print(re.sub("\s", " space ", txt))
print(re.sub("\s", " space ", txt, 2))  # replaces the first two occurances.

#7. match object
print("\n7.")
txt= "The rain in Spain"
x= re.search(r"\bS\w+", txt)
    # What r"\bS\w+" means
        # a "raw string"(r) that starts with the letter "S"(\bS), and contains any more other 
        # characters(\w) with one or more occurances(+).

        # so instead of r"\bS\w+", you can write r"\bS.+"
print(x.span())
print(x.string)
print(x.group())    # look for any words that starts with the letter "S"


"""
1. REgEx functions
function            description
findall             returns a list containing all matches.
search              returns a match object if there is a match anywhere in the string.
split               returns a list where the string has been split at each match.
sub                 replaces one or many matches with a string.

2. metacharacers are chars with special meaning.
    like in C, when you use a FILE IO to fscanf the shit.
    if there is a match, returns the exact match.
        ex) if you write "he.{2}o" and there is indeed "hello", returns "hello".
    if there's not, then returns none(False).

    CHARACTER           DESCRIPTION                         EXAMPLE
    []                  a set of characters                 "[a-m]"         all lower cases between a, m
    \                   signals a special sequence          "\d"    "\s"    decimals, strings
                        (can also be used to escape)    
    .                   any character(except newline)       "he..o"         hello, heppo, hesko ...etc
    ^                   starts with                         "^hello"
    $                   ends with                           "world$"
    *                   zero or more occurances             "he.*o"         heo, helo, hello, hellllo...
    +                   one or more occurances              "he.+o"         same w above, but not "heo"
    ?                   zero or one occurance               "he.?o"         heo, helo, hepo, etc...
    {}                  exactly the specified number        "he.{2}o"       hello, heplo, helpo etc...
                        of occurances
    |                   either or                           "fails|stays"      


3. below is all the Special Sequences that can be used for he metachar, "\"

Character	Description	                                                        Example	
\A	        Returns a match if the specified characters are at the beginning    "\AThe"	
            of the string	                                                    
\b	        Returns a match where the specified characters are at the           r"\bain"
            beginning or at the end of a word                                   r"ain\b"	
                (the "r" in the beginning is making sure that the string is 
                being treated as a "raw string")	                            
                                                                                
\B	        Returns a match where the specified characters are present, but     r"\Bain"
            NOT at the beginning (or at the end) of a word                      r"ain\B"	
                (the "r" in the beginning is making sure that the 
                string is being treated as a "raw string")	                    
                                                                                	
\d	        Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	        Returns a match where the string DOES NOT contain digits	        "\D"	
\s	        Returns a match where the string contains a white space character	"\s"
                주의!!!!!!!
                python 에서 \s는 string 이; 아니라, white space, 즉 공백이다!!!!!!!
                [\t\n\r\f\v] 라고 볼 수 있음.
                    \t(tap), \n(새 줄,Line Feed), \r(Carriage Return), \f(Form feed)
\S	        Returns a match where the string DOES NOT                           "\S"        
            contain a white space character
                ==[^\t\n\r\f\v]	                                   	
\w	        Returns a match where the string contains any word characters       "\w"
            (characters from a to Z, digits from 0-9,                       
            and the underscore _ character)	                                    	
\W	        Returns a match where the string DOES NOT                           "\W"
            contain any word characters	                                        
\Z	        Returns a match if the specified characters                         "Spain\Z"
            are at the end of the string	                                    


Sets
below are the sets that can be used in the metachar, in [].

Character   description
[arn]	    Return  s a match where one of the specified characters (a, r, or n) are present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]  	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a 
            match for any + character in the string


4. .findall() finds all matches, while
    .search() finds only the first occurance that makes a match.


7. match object
the match object has several methods and properties of its own.
    .span()     : returns a tuple containing the start and end positions of the match.
    .string     : returns the string passed into the function.
    .group()    : returns the part of the string where there was a match.

        if there is no match, the value "none" will be returned instead of the "match" object.
"""