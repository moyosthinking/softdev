//Team Popcorn :: Moyo Fagbuyi, Sasha Murokh
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
let fact = function (n) {if (n == 1) {return 1;} else { return (n *(fact (n -1))); } } 


//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
//(fact 1) "...should be  1"
//(fact 2) "...should be  2"
//(fact 3) "...should be  6"
//(fact 4) "...should be  24"
//(fact 5) "...should be  120"


//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
let fib = function (n) {if (n == 0) {return 0;} if (n == 1) {return 1;} else {return (fib(n - 2)) + (fib(n - 1));}} 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
//(fib 0) "...should be  0"
//(fib 1) "...should be  1"
//(fib 2) "...should be  1"
//(fib 3) "...should be  2"
//(fib 4) "...should be  3"
//=================================================================
