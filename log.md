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


## Codeforces 2033 D (1300) (2024-01-03) (33 min)

### Success
YES

### Good
- Solved in first submission
- I was able to find the correct approach by analyzing the problem with pen and paper, and skectched a proof

### Bad
- My initial implementation was wrong, it was more complicated than it needed to be. That made me introduce a bug, luckily I was able to spot it before submitting

### Action items

#### Questions I should have asked
- Can I make this logic simpler?


## Codeforces 2033 C (1400) (2024-01-03) (30 min)

### Success
NO

### Good
- I thought correctly the structure of the solution, but I failed with a detail that caused edge cases

### Bad
- I was not able to see that my solution would hit and edge case in the way I solved it
- I am still not sure if I would have been able to come up with the solution that works on all cases

### Action items
- Always validate the solution. Try to break it
- Try to divide the problem in different cases to find edge cases

#### Questions I should have asked
- Can this problem be divided into cases?
- Can I think of a case that will break this solution?


## Codeforces 2032 C (1400) (2024-01-03) (1h+)

### Success
NO

### Good

### Bad
- I thought I had a solution, but it hitted multiple edge cases
- Missunderstood "For every pairwise distinct triplet of indices", I was thinking abount "items" in the array, not indeces
- Spent more time than assigned
- I do not understand the editorial

### Action items
- DO NOT SPEND MORE TIME THAN THE ASSIGNED!!!!
- Decrease dificulty to 1200

#### Questions I should have asked


## Codeforces 2021 B (1200) (2024-01-03) (30 min)

### Success
NO

### Good

### Bad
- I worked in a solution which was incorrect

### Action items
- Validate solutions before start coding
- Decrease dificulty to 1000

#### Questions I should have asked
- Does this solution give the required answer?


## Codeforces 1773 F (800) (2024-01-04) (32 min)

### Success
YES

### Good
- Solved in first attempt

### Bad
- Spent more than 30 minutes

### Action items
- Identify points where the strategy might change
- Think of different scenarios

#### Questions I should have asked
- Is there a value that can take variable X that makes the solution easier? or harder?


## Codeforces 2050 A (800) (2024-01-05) (8 min)

### Success
YES

### Good
- Solved in first attempt

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2049 A (800) (2024-01-05) (27 min)

### Success
YES

### Good
- Solved in less than 30 minutes
- I was able to identify the possible values of the outputs

### Bad
- Failed first attempt because I did not consider a scenario
- My solution is complicated

### Action items

#### Questions I should have asked
- Can this case be generalized to include more cases?


## Codeforces 2048 A (800) (2024-01-05) (10 min)

### Success
YES

### Good
- Solved in the first attempt
- I was able to identify the condition hidden in the question (being multiple of 33) 

### Bad
- I was not able to prove that it would work in every case. I was lucky that it passed all the tests. (I know I can prove it, but I did not want to spend the time, now that I know that it works I will prove it)

### Action items

#### Questions I should have asked


## Codeforces 2047 A (800) (2024-01-05) (11 min)

### Success
YES

### Good
- Solved in the first attempt
- I was able to identify the condition hidden in the question (square of an odd number)

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2048 B (900) (2024-01-06) (17 min)

### Success
YES

### Good
- Solved in the first attempt
- Same solution as in the editorial

### Bad
- I had to reread the problem statement because at first I miss undertsood it
- I did not know from the top of my mind a way to construct the permutation if I needed to reserve some items to put it in strategic places. I had to come up with a way, it would have been nice to know this by heart

### Action items
- Study an algorithm to build permutations reserving items

#### Questions I should have asked


## Codeforces 2047 B (900) (2024-01-06) (26 min)

### Success
YES

### Good
- Solved in less than 30 min
- I realized how to solve the problem relatively quickly
- Same solution as in the editorial

### Bad
- My first attempt was incorrect
- Although I knew how to solve the problem, I was not able to write the implementation quickly. I knew there were some edge cases that I would have to deal with (such as when all the characters are the same, or when all characters had the same frequency). This made me lose a lot of time
- It was hard for me to come up with a way to compute the max and min elements. I had to change the implementation completely because I was hitting a bug

### Action items
- Study an algorithm to find the max and min frequency elements from a list

#### Questions I should have asked


## Codeforces 2042 B (900) (2024-01-06) (12 min)

### Success
YES

### Good
- Solved in first attempt
- Same solution as in the editorial

### Bad
- My first implementation had a bug, but I was able to spot it with the local tests

### Action items
- Make sure that each step in the implementation is correct

#### Questions I should have asked
- Is this step correct?


## Codeforces 2035 B (900) (2024-01-06) (23 min)

### Success
YES

### Good
- Solved in first attempt
- Same solution as in the editorial (with a minor implementation detail, but the overall idea is the same)

### Bad
- I was not able to formally prove that the solution would work, however, from experimentation I was pretty confident. Still, I had doubts when I submitted the solution
- I had 7 more minutes to try and prove, but I was not confident that I would succeed
- I feel I could have solved it faster if I had asked the right questions, or looked for patterns earlier

### Action items

#### Questions I should have asked
- Is there a pattern in the test cases?
- Do odd and even make a difference?


## Codeforces 2040 B (1000) (2024-01-07) (26 min)

### Success
YES

### Good
- Solved in first attempt
- Same solution as in the editorial

### Bad
- I felt I would not be able to solve it in less than 30 minutes. I got really nervous towards the end

### Action items
- Keep calm and trust in yourself

#### Questions I should have asked


## Codeforces 2039 B (1000) (2024-01-07) (34 min)

### Success
YES

### Good

### Bad
- I used more than 30 minutes
- I did not think of edge cases, my first submission was incorrect
- I made a silly bug which caused a TLE
- I did not started the timer later (15 minutes after starting approx), so I am not sure of the time I spent

### Action items
- Decrease difficulty to 900

#### Questions I should have asked
- Can I break this solution?
- Is there a case where this solution does not give the correct answer?


## Codeforces 2033 B (900) (2024-01-07) (21 min)

### Success
YES

### Good
- Solved it in first attempt

### Bad
- Spent a lot of time figuring out how to iterate over the diagonals of a matrix

### Action items
- Study how to iterate over the diagonals of a matrix

#### Questions I should have asked


## Codeforces 2031 B (900) (2024-01-07) (41 min)

### Success
YES

### Good
- Could not solve it in less than 30 min

### Bad
- Spent a lot of time figuring out how the correct solution
- Made a mistake in my first implementation, bug in logic

### Action items
- Go back to 800

#### Questions I should have asked
- Is this condition sufficient or just necessary?


## Codeforces 2042 A (800) (2024-01-08) (12 min)

### Success
YES

### Good
- First attempt

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2040 A (800) (2024-01-08) (16 min)

### Success
YES

### Good
- First attempt

### Bad
- Had several bugs during the implementation, but I could find them with the local tests

### Action items

#### Questions I should have asked
- Is this step correct?
- What is the answer space?


## Codeforces 2039 A (800) (2024-01-08) (12 min)

### Success
YES

### Good
- First attempt
- Could deduce the optimal solution using math and prove it

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2038 A (800) (2024-01-08) (7 min)

### Success
YES

### Good
- First attempt

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2028 A (900) (2024-01-09) (17 min)

### Success
YES

### Good

### Bad
- My first attempt failed, however, the mistake wasn't a big deal

### Action items

#### Questions I should have asked


## Codeforces 2026 A (900) (2024-01-09) (27 min)

### Success
YES

### Good
- First attempt

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2013 B (900) (2024-01-09) (19 min)

### Success
YES

### Good
- First attempt
- Came up with a formula to compute the result

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2007 B (900) (2024-01-09) (19 min)

### Success
YES

### Good
- First attempt

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2051 C (1000) (2024-01-10) (19 min)

### Success
YES

### Good
- I was able to divide the problem into cases

### Bad
- I tried to be smart in the implementation trying to use fancy iterators instead of a simple for loop, which cause me to introduce a bug in my first attempt

### Action items
- Resist the urge to be smart. Keep things simple

#### Questions I should have asked


## Codeforces 2037 C (1000) (2024-01-10) (14 min)

### Success
YES

### Good
- First attempt
- I was able to come up with a mathematical solution, and proved that work on all cases
- I resisted the urge to be smart on the implementation

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2034 B (1000) (2024-01-10) (12 min)

### Success
YES

### Good
- First attempt

### Bad
- I had a bug in the first implementation, but could find it during local testing

### Action items

#### Questions I should have asked
- Is this step correct?
- Am I doing everything I need to do for this case / if this happens?


## Codeforces 2005 B1 (1000) (2024-01-10) (45+ min)

### Success
YES

### Good
- I was able to come up with a general plan to solve the problem dividing the problem in different cases

### Bad
- I was slow to implement the solution
- My first submission was after the initial 30 mins, and it was incorrect
- I had some off by one errors

### Action items
- Keep practicing
- Go back to 900

#### Questions I should have asked


## Codeforces 2005 A (900) (2024-01-11) (14 min)

### Success
YES

### Good
- First attempt
- First implementation
- Proved that the solution was optimal

### Bad

### Action items

#### Questions I should have asked


## Codeforces 1992 C (900) (2024-01-11) (15 min)

### Success
YES

### Good
- First attempt
- First implementation
- Proved that the solution was optimal

### Bad

### Action items

#### Questions I should have asked


## Codeforces 1990 A (900) (2024-01-11) (35 min)

### Success
YES

### Good

### Bad
- Spent more than 30 minutes
- My first attempt was incorrect, the logic was wrong
- I found the correct solution on time, but was not able to implement the logic in code

### Action items
- Study how to count the number of times an element appears in an array
- Go back to 800

#### Questions I should have asked


## Codeforces 2053 A (800) (2024-01-11) (15 min)

### Success
YES

### Good
- First attempt

### Bad
- First implementation was incorrect, but was able to find the problem in local tests

### Action items

#### Questions I should have asked


## Codeforces 2051 B (800) (2024-01-12) (11 min)

### Success
YES

### Good
- First attempt

### Bad
- First implementation was incorrect, but was able to find the problem in local tests

### Action items

#### Questions I should have asked


## Codeforces 2051 A (800) (2024-01-12) (7 min)

### Success
YES

### Good
- First attempt
- First implementation

### Bad

### Action items

#### Questions I should have asked


## Codeforces 2043 A (800) (2024-01-12) (10 min)

### Success
YES

### Good

### Bad
- First implementation was incorrect

### Action items
- Avoid trying to be smart. Go for the simpler solution

#### Questions I should have asked


## Codeforces 1988 B (900) (2024-01-13) (8 min)

### Success
YES

### Good
- First attempt
- First implementation

### Bad

### Action items

#### Questions I should have asked


## Codeforces 1988 B (900) (2024-01-13) (8 min)

### Success
YES

### Good
- First attempt

### Bad
- My initial implementation was incorrect, but could catch the bug during local testing

### Action items
- Keep things simple, if a simple loop is enough, then do that

#### Questions I should have asked
