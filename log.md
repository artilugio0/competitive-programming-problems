## Codeforces 2038 L (1400) (2024-12-30)

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

## Codeforces 2049 B (1300g (2024-12-30g (45 ging

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
