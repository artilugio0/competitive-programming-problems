## Codeforces 2038 L (1400) (2024-12-30)

### Success
YES

### Good
* I quickly realized that this could be solved using a greedy algorithm

### Bad
* I used too much time trying to solve it. (I said I would dedicate 30 min, and look at the editorial if I could not solve it, but instead ended up using more than 1h because I though I was near, and kept extending the time limit).
* I considered the greedy approach, but did not finish the analysis, which led me to an incorrect greedy approach. I should have analyzed all (or at least more) alternatives.
* Got stuck computing a reminder. There weren't so many possible values for that reminder, I should have listed all possible cases after trying for a couple of minutes. Anyways... the approach was incorrect (at that time I did not know that), so if I have done that I would have realized that the approach was incorrect earlier.
* I do not feel comfortable with rounding. I am not sure what ends up happening if I round down and then up for example.

### Action items
* Comply with the time limit I set. (If I realize that I always hit the time limit, I can adjust it for future problems)
* Use pen and paper, do not analyze just in my head for more than 1 minute
* Do not jump to coding until I see a clear path to the solution.
* Don't try to be smart by default. If I have a smart idea and a dumb idea that both solve the problem, if I'm having trouble implementing the smart idea for a couple of minutes, go for the dumb idea.
* Study math.floor, math.ceil, and their combinations. Also study their relations with reminders.

#### Questions I should have asked
* What are ALL of the the optimal combinations?
* Will always choosing any optimal combination lead me to the correct answer?


## Codeforces 2049 C (1500) (2024-12-30)

### Success
YES

### Good
* I was able to solve it first try.
* I used pen and paper to understand the problem, create a solution and validate it.
* I did not try to be smart when creating the list of friends, since the number of friends was always 2 or 3.
* I did not try to be smart when checking for the values in the array, there were only 3 possible values so I iffed between the 3 values.

### Bad
* I started trying to come up with a solution without first reading the notes that explained the examples. Initially I missunderstood the problem, so the examples given did not match my expectations. It was only when I read the notes that explained the examples that I really understood the problem. This made me waste some minutes.
* I spent more than 30 minutes, but I was almost finishing the solution by then, so it is not a big issue.
* I forgot to start a timer after the first 30 minutes were over, so I am not sure if I spent a lot of time after the first 30 mins. I feel that it was less than 10 minutes.
* I should have noticed faster that the amount of friends was always 2 or 3, and that that meant that a solution could always be built using only the numbers 0, 1 and 2.

### Action items
* Make sure to always read the notes after the examples
* Use a time counter instead of a countdown, so that I do not have to be thinking about restarting the timer, etc
* When understanding the problem and coming up with a solution, try to first identify some properties or invariants of the problem that might be useful for or simplify the solution

#### Questions I should have asked
- Are the values that appear in the example outputs contained in a range or share a property? (for example, here all numbers where between 0 and 2)
- What are the lower and upper bounds of X? (for example, here the lower and upper bounds of the amount of friends a dragon can have were 2 and 3)


## Codeforces 2046 A (1200) (2024-12-30) (43 min)

### Success
YES

### Good
- I was able to solve it in less than 45 min
- I was able to understand the problem fairly quickly, and understand how all the examples worked

### Bad
- I needed multiple attempts because I kept hitting edge cases
- I did not spend enough time with pen and paper, initially I thought the solution without pen and paper. Later I realized that I should validate it with pen and paper, but I only tried 1 case.
- After my first wrong attempt, I added an if for the specific edge case, but did not stop to think if there were any other cases that I was not handling

### Action items
- ALWAYS use pen and paper, at least until I become somewhat good at this
- ALWAYS think of possible ways of breaking my algorithm
- Use assert in the code to ensure invariants hold (for example, in this problem after iterating all columns at some point the shift from row1 to row2 must have happened. I made a mistake which allowed this not to happen. An assert could have avoided a wrong attempt)

#### Questions I should have asked
- What happens in the extreme cases? (minimal / maximal inputs)
- What happens in the turning points, are there more than one way the turning point can happen? (for example, in this problem a decision had to be made to switch from one row to the other one, it turns out that the switch could be done in two different situations with different results)
- What are the invariants in the problem?
- What are the invariants in the solution?


## Codeforces 2049 B (1300) (2024-12-30) (45 min)

### Success
NO

### Good

### Bad
- Was not able to solve it
- I spent all the time thinking a solution in pen and paper, did not write any code
- I have no idea how I could have figured it out, it is difficult to find action items
- I realized some special cases where I could find an answer, maybe I should have at least tried to code those cases

### Action items
- Think about the properties of the system. For example, I knew that a string where a p comes before an s was impossible. If I kept looking for those properties, I might have found the solution

#### Questions I should have asked
- What properties / invariants does the problem have? (this is the second time I write this)


## Codeforces 2041 E (1200) (2024-12-31) (14 min)

### Success
YES

### Good
- Was able to solve it
- The first solution I thought of was correct
- I took my time with pen an paper to validate the idea
- I mathematically proved that the idea was correct

### Bad
- My first attempt was incorrect because I forgot to print the length of the array, I just printed the array

### Action items
- Vefify that the output structure matches the outputs in the examples

#### Questions I should have asked


## Codeforces 2037 D (1300) (2024-12-31) (34 min)

### Success
YES

### Good
- Was able to solve it in the first attempt
- The first solution I thought of was correct
- I took my time with pen an paper to validate the idea
- I came up with the same solution idea as the one in the editorial
- The max heap solution I came up with is the same as in the editorial code

### Bad
- Had to look how to implement a max heap in python, the standard library only has a min heap implementation. Ended up negating the values
- When trying locally, I hitted an out of bounds error while iterating an array. I have to internalize that I must check bounds before accessing an array by index

### Action items
- Ensure I ALWAYS check bounds before accessing by index

#### Questions I should have asked


## Codeforces 2038 C (1400) (2024-12-31) (36 min)

### Success
YES

### Good
- Was able to solve it in the first attempt
- The first solution I thought of was correct, except for one edge case that I found during my tests

### Bad
- There was an edge case that I was able to solve, however, I did not understand the solution when I submitted the solution, so I was not certain that I was covering all cases
- It was possible fix the edge case adding an extra if, that would have ensured that the solution was correct

### Action items
- Try to force correct solutions with code if unsure. For example, in this problem switching x2 for y2 solved the issue, but I did not understand why. A better solution would have been to compute the area with and without the switch, and keep the values that maximized the area

#### Questions I should have asked
- Can I add a condition to guarantee that the answer will be correct?


## Codeforces 2050 E (1500) (2024-01-01) (3 hs)

### Success
YES

### Good
- Was able to desing the correct solution in less than 30 minutes.

### Bad
- The first implementation I made with recursive DP hit the recursion limit, so I got a runtime error
- I implemented an iterative DP solution and hit the time limit
- When I looked at the editorial, my solution was correct, but it seems that python is too slow for some reason. I implemented both iterative and recursive DP solutions in golang with the same logic and both got accepted
- After the reading the editorial I spent a lot of time trying to understand why my solution did not work. I ended up implementing it in golang just to validate if my logic was incorrect

### Action items
- Migrate to C++, Rust or Golang

#### Questions I should have asked


## Codeforces 2041 B (1200) (2024-01-01) (1+ hs)

### Success
NO

### Good

### Bad
- Was not able to solve it
- I feel I could have solved it if I tried to find out more about the problem properties
- I focused on coming up with an algorithm instead of taking time to find out invariants / properties

### Action items
- Dedicate more time to invariant, properties
- Whenever I know of a necessary condition to solve the problem, I MUST ask if that condition is also sufficient. In this case it was, If i had enough pins, then that was sufficient to know that an arrangement existed

#### Questions I should have asked
- Is this neccesary condition also a sufficient condition?


## Codeforces 2041 B (1200) (2024-01-01) (unknown)

### Success
YES

### Good
- I was able to solve it
- Although my first attempt hit a time limit, the code was correct. Using PyPy with the same code all tests passed

### Bad
- My clock run out of battery, so I don't have idea how much time I spent in the problem. I feel that it was less than an hour in total
- I tried troubleshooting my code instead of first trying with PyPy

### Action items
- Always try with PyPy if the python solution reachs a time limit
- Migrate to C++ / Golang / Rust

#### Questions I should have asked


## Codeforces 2038 A (1400) (2024-01-01) (34 min approx)

### Success
YES

### Good
- I was able to solve it on the first try

### Bad
- I forgot to time my resolution

### Action items

#### Questions I should have asked


## Codeforces 2038 A (1200) (2024-01-02) (1 h approx)

### Success
NO

### Good

### Bad
- Did not know how to approach the problem
- I was unsure if I could brute force over a value ~ 10**7
- Did not know what relevant questions to ask myself

### Action items
- Learn more about time complexity, when is it ok to iterate over results? aka: how many ops can I perform per second in a safe way?
- Learn more about bitwise operations
- With problems related to bitwise operations, always think in terms of powers of 2

#### Questions I should have asked
- Is it ok to bruteforce over this range?
- Is there a way to find an upper bound to the value of X (lower that the one given in the problem statement)?
- Can this problem be divided into cases?


## Codeforces 2035 C (1400) (2024-01-02) (2 h)

### Success
NO

### Good
- I had an idea of how to solve it, but could not figure out the details

### Bad
- Could not solve it, even reading the editorial

### Action items
- Learn more about bitwise operations
- NEVER USE MORE TIME THAN WHAT I HAVE INITIALLY ASSIGNED!!!!!

#### Questions I should have asked
- Can this problem be divided into cases?
- Can I find cases where the solution is easy?


## Codeforces 2034 C (1400) (2024-01-02) (45 min + extra for implementation in golang)

### Success
YES

### Good
- I was able to come up with a correct solution in my first attempt

### Bad
- The implementation in python was too slow. I had to migrate it to golang to pass all tests

### Action items
- Start using C++ / Rust

#### Questions I should have asked


## Codeforces 2033 E (1400) (2024-01-02) (1 h)

### Success
NO

### Good

### Bad
- I was not able to come up with the correct solution.
- I though I had it. Had some trouble implementing it, but I hitted an edgecase that made my solution incorrect
- I spent too much time once again, I was sure that my approach was correct, but it wasnt

### Action items
- Stop when time is up, always. No matter if I think that the ongoing implementation is the correct solution. This will help me utilize my time more efficiently

#### Questions I should have asked
- Can I prove that my approach is correct?
