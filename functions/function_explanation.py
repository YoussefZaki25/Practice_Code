'''
Functions explained:

There's this idea in code of trying to do the least amount of work possible and not re creating the wheel.  Basically what people mean by this is that you shouldn't
try to create something that has already been created before.  Hence, don't recreate the wheel, as a phrase.

I'm going to show you two different pieces of code that do the same thing. Then give an explanation for whats different between them.
'''

first_number = 1
second_number = 2
result = first_number + second_number
print(result)

def add(first_number, second_number):
  return first_number + second_number

print(add(1,2))
print(add(4,7))

'''
Okay so the first block of code I want you to look at is in lines 10-13.  First we create a variable with an integer data type called "first_number", and we set it to 1.

Next, we create another variable called "second_number" with an integer data type that has the value of 2.

Third, we set a new variable type to be equal to both of these variables being added together.  That new variable is called "result"

Lastly, we print the result and it returns the number 3.

But what happens if we want to add different numbers?  Without a function, we would have to rewrite lines 10-13 over and over and over again every time we wanted to add
different numbers.

Lines 15-16 show how to create a function.  The first keyword "def" basically tells python we're creating a function.  The name "add" can be replaced with whatever you
want but you should name it to whatever the function does so in our case the function adds numbers.  The next part is a little trick to explain.

Remember that we are creating a function so that we can take in different numbers without having to rewrite the same code.  Keeping that in mind, the parenthesis
is the section where you say how many things your function is going to need to know in order to be able to run.

In our function declaration on line 15, we are basically saying to python, "we are creating a function that needs 2 numbers, one called first_number and another
called second_number.

Then, when we want to add two numbers again, instead of rewriting the code over and over again, now we just call our function and put in the parenthesis the numbers
we want to add.  This way we can use different numbers in any way and it will always add the two numbers.

Try and call the function adding whatever 2 numbers you want. Then push back to this repo
'''
