[TOC]



## Self introduction

Make an elevator pitch: **Short, Direct, Attention-grabbing**. You should not spend too much time on self-introduction under 1 or 2 mins or you will have less time on coding.

Start with Basic background Info-don’t dive into deeper- they will ask u the one they are interested.

- Internships and Full-time
- THINK what  they want me - tech stack

## Best end of interview questions to ask

### Best questions to ask for knowing more about technical work

- **What are the engineering challenges that the company/team is facing?**
- **What has been the worst technical blunder that has happened in the recent past? How did you guys deal with it? What changes were implemented afterwards to make sure it didn't happen again?**
- **What is the most costly technical decision made early on that the company is living with now?**
- **What is the most fulfilling/exciting/technically complex project that you've worked on here so far?**
- **I do/don't have experience in domain X. How important is this for me to be able to succeed?**
- How do you evaluate new technologies? Who makes the final decisions?
- How do you know what to work on each day?
- How would you describe your engineering culture?
- How has your role changed since joining the company?
- What is your stack? What is the rationale for/story behind this specific stack?
- Do you tend to roll your own solutions more often or rely on third party tools? What's the rationale in a specific case?
- How does the engineering team balance resources between feature requests and engineering maintenance?
- What do you measure? What are your most important product metrics?
- How often have you moved teams? What made you join the team you're on right now? If you wanted to move teams, what would need to happen?
- What resources does the company have for new hires to study its product and processes? Are there specifications, requirements, documentation?
- How do you think my expertise would be relevant to this team? What unique value can I add?

### Best questions to ask for knowing more about the role

- **What qualities do you look out for when hiring for this role?**
- **What would be the most important problem you would want me to solve if I joined your team?**
- What does a typical day look like in this role?
- What are the strengths and weaknesses of the current team? What is being done to improve upon the weaknesses?
- What resources does the company have for new hires to study its product and processes? Are there specifications, requirements, documentation?
- What would I work on if I joined this team and who would I work most closely with?

### Best questions to ask for knowing more culture and welfare

- **What is the most frustrating part about working here?**

- **What is unique about working at this company that you have not experienced elsewhere?**

- **What is something you wish were different about your job?**

- How is individual performance measured?

- What do you like about working here?

- What is your policy on working from home/remotely?

- What does the company do to nurture and train its employees?

- Does the company culture encourage entrepreneurship and creativity? Could you give me any specific examples?

  

### Best questions to ask to know more about team leadership or management

These questions are suitable for asking Engineering Managers or senior level management, such as CEO, CTO, VPs and are especially useful for the Team Matching phase of Google interviews or post-offer calls that your recruiters set up with the various team managers.

- **How do you train/ramp up engineers who are new to the team?**
- **What does success look like for your team/project?**
- **What are the strengths and weaknesses of the current team? What is being done to improve upon the weaknesses?**
- **Can you tell me about a time you resolved an interpersonal conflict?**
- How did you become a manager?
- How do your engineers know what to work on each day?
- What is your team's biggest challenge right now?
- How do you measure individual performance?
- How often are 1:1s conducted?
- What is the current team composition like?
- What opportunities are available to switch roles? How does this work?
- Two senior team members disagree over a technical issue. How do you handle it?
- Have you managed a poor performer at some point in your career before? What did you do and how did it work?
- Where do you spend more of your time, high performers or low performers?
- Sometimes there's a trade-off between what's best for one of your team members and what's best for the team. Give an example of how you handled this and why.
- Give an example of a time you faced a difficult mentoring/coaching challenge. What did you do and why?
- What is your management philosophy?
- What is the role of data and metrics in managing a team like ours?
- What role does the manager play in making technical decisions?
- What is an example of a change you have made in the team that improved the team?
- What would be the most important problem you would want me to solve if I joined your team?
- What opportunities for growth will your team provide?
- What would I work on if I joined this team and who would I work most closely with?

### Best questions to ask to know more about company direction

- **How does the company decide on what to work on next?**
- What assurance do you have that this company will be successful?
- Which companies are your main competitors and what differentiates your company?
- What are your highest priorities right now? For example, new features, new products, solidifying existing code, reducing operations overhead?



# For Virtual onsite coding interviewing

- [ ] Dress comfortably
- [ ] Prepare pen and paper
- [ ] Use earphones or headphones and make sure you are in a quiet environment
- [ ] Check that your internet connection is working
- [ ] Check that your webcam and audio are working
- [ ] Familiarize and set up shortcuts in the coding environment (CoderPad / CodePen)
- [ ] Turn off the webcam if possible

# For Phone screen coding interviews

- [ ]  Use earphones and put the phone on the table
- [ ] Request for the option to use Zoom/Google Meet/Hangouts or Skype instead of a phone call

# For onsite whiteboarding coding interviews

- [ ]  Learn about whiteboard space management

# What to do during your coding interview

## 1 Introduction

See [Self introduction ](#Self introduction)

## 2 Upon receiving the question, make clarifications

**Do not jump into coding right away.** Coding questions tend to be vague and underspecified on purpose to allow the interviewer to gauge the candidate's attention to detail and carefulness. **Ask 2-3 clarifying question.**

- [ ] Paraphrase and repeat the question back at the interviewer.

  ```
  Make sure you understand exactly what they are asking
  ```

  

- [ ] Clarify assumption

- > A tree-like diagram could very well be a graph that allows for cycles and a naive recursive solution would not work. Clarify if the given diagram is a tree or a graph.

- > Can you modify the original array / graph / data structure in any way?

- > How is the input stored?

- > If you are given a dictionary of words, is it a list of strings or a Trie?

- > Is the input array sorted? (e.g. for deciding between binary / linear search)

- [ ] Clarify input value range.

  > Inputs: how big and what is the range?

- [ ] Clarify input value format

  > Values: Negative? Floating points? Empty? Null? Duplicates? Extremely large?

- [ ] Work through a simplified example to ensure you understood the question.

  > E.g., you are asked to write a palindrome checker, before coding, come up with simple test cases like "KAYAK" => true, "MOUSE" => false, then check with the interviewer if those example cases are in line with their expectations.

  

## 3 Work out and optimize your approach with the interviewer

The worst thing you can do next is jump straight to coding - interviewers expect there to be some time for a 2-way discussion on the correct approach to take for the question, including **analysis of the time and space complexity.**

This discussion can range from a few minutes to up to 5-10 minutes depending on the complexity of the question. This also gives interviewers a chance to provide you with hints to guide you towards an acceptable solution.

- [ ]  If you get stuck on the approach or optimization, use [this structured way](#how to think\) to jog your memory  find a good approach
- [ ]  Explain a few approaches that you could take at a high level (don't go too much into implementation details). Discuss the **tradeoffs** of each approach with your interviewer as if the interviewer was your coworker and you all are collaborating on a problem.
- [ ] State and explain the [time and space complexity of your proposed approach(es](# how to optimize your approach))
- [ ] [Agree on the most ideal approach and optimize it. Identify repeated/duplicated/overlapping computations and reduce them via caching.](# how to optimize your approach)

==Don’t do that==

1. Do not jump into coding right away
2. Do not ignore any piece of information given
3. Do not appear unsure about your approach or analysis

### How to think

1. Visualize the problem by drawing it out

2. Think about how you would solve the problem by hand

3. Come up with more examples

4. Break the question down into smaller independent parts

5. Apply common data structures and algorithms at the problem

   ```
   These are the data structures to keep in mind and try, in order of frequency they appear in coding interview questions:
   
   Hash Maps: Useful for making lookup efficient. This is the most common data structure used in interviews and you are guaranteed to have to use it.
   Graphs: If the data is presented to you as associations between entities, you might be able to model the question as a graph and use some common graph algorithm to solve the problem.
   Stack and Queue: If you need to parse a string with nested properties (such as a mathematical equation), you will almost definitely need to use stacks.
   Heap: Question involves scheduling/ordering based on some priority. Also useful for finding the max K/min K/median elements in a set.
   Tree/Trie: Do you need to store strings in a space-efficient manner and look for the existence of strings (or at least part of them) very quickly?
   ```

   **Routines**

   - Sorting
   - Binary search: Useful if the input array is sorted and you need to do faster than O(n) searches
   - Sliding window
   - Two pointers
   - Union find
   - BFS/DFS
   - Traverse from the back
   - Topological Sorting

### How to optimize your approach

#### How to optimize time complexity

#####  1 Identify the Best Theoretical Time Complexity of the solution

The Best Theoretical Time Complexity (BTTC) of a solution is a time complexity you know that you cannot beat.

If your initial solution is slower than the BTTC, there could be opportunities to improve such that you can attain the BTTC (but not always the case). It would**<u>n't hurt to mention the BTTC to your interviewer</u>**, which will be taken as a positive signal and also to remind yourself that you should **<u>not try to come up with something faster than the BTTC</u>**.

Pay attention to detail given about the question. Be careful not to determine the incorrect BTTC due to lack of attention to the question details!

 If your solution already has the BTTC and the interviewer is asking you to optimize further, there are usually <u>**two things they are looking out fo**</u>r:

- Do even less work. Your solution could be O(n) but making two passes of the array and the interviewer is looking for the solution that uses a single pass.
- Use less space. Refer to the section below on optimizing space complexity.

#####  2 Identify overlapping and repeated computation

Bruce force often excutes the same operation over and over again.

Try to use dynamic programing and Non-DP programing.

**eg.** The [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) question is a good example of a problem which contains overlapping/repeated work. To get the value for an index, you need to multiply the values at all other positions. Doing this for every value in the array would take O(n2) time. However, see that:

- `result[n]`: `Product(nums[0] … nums[n-1]) * Product(nums[n + 1] … nums[N - 1])`
- `result[n + 1]`: `Product(nums[0] … nums[n]) * Product(num[n + 2] … nums[N - 1])`

There's a ton of duplicated work in computing the `result[n]` vs `result[n + 1]`! This is an opportunity to reuse earlier computations made while computing `result[n]` to compute `result[n + 1]`. Indeed, we can make use of a prefix array to help us arrive at the final solution in O(n) time at the cost of more space.

##### 3 Try different data structures

[Ex](https://www.techinterviewhandbook.org/coding-interview-techniques/#example-4)

The [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) question can be solved in a naive manner by calculating the distance of each point, sorting them and then taking the K smallest values. This takes O(nlog(n)) time because of the sorting. However, by using a Heap data structure, the time complexity can be reduced to O(nlog(k)) as adding/removing from the heap only takes O(log(k)) time when the size of the heap is capped at K elements. Changing the data structure made a whole ton of difference to the efficiency of the algorithm!

##### 4. Identify redundant work

1. Don't check conditions unnecessarily

2. Mind the order of checks

   ```
   if slow() or fast() - There are two operations in this check, of varying durations. As long as one of the operations evaluates to true, the condition will evaluate to true. Most computers execute operations in order from left to right, hence it is more efficient to put the fast() on the left.
   if likely() and unlikely() - This example uses a similar argument as above. If we execute unlikely() first and it is false, we don't have to execute likely().
   ```

3. Don't invoke methods unnecessarily

   ```
   If you have to refer to a property multiple times in your function and that property has to be derived from a function call, cache the result as a variable if the value doesn't change throughout the lifetime of the function. The length of the input array is the most common example. Most of the time, the length of the input array doesn't change, declare a variable at the start called length = len(array) and use length in your function instead of calling len(array) every time you need it.
   ```

4. Early termination
   Don’t do the unnecessary check!

5. Minimize work inside loops

   ```python
   def contains_string(search_term, strings):
     for string in strings:
       if string.lower() == search_term.lower():
         return True
     return False
   ```

   ```python
   def contains_string(search_term, strings):
     search_term_lowercase = search_term.lower()
     for string in strings:
       if string.lower() == search_term_lowercase:
         return True
     return False
   ```

   Don’t do unnecessary code!

6. Be lazy

   Lazy evaluation is an evaluation strategy which delays the evaluation of an expression until its value is needed. Let's use the same example as above. We could technically improve it a little bit:

   ```python
   def contains_string(search_term, strings):
     if len(strings) == 0:
       return False
     # Don't have to change the search term to lower case if there are no strings at all.
     search_term_lowercase = search_term.lower()
     for string in strings:
       if string.lower() == search_term_lowercase:
         return True
     return False
   ```





#### How to optimize space complexity

##### 1. Changing data in-place/overwriting input data

The [Dutch National Flag](https://leetcode.com/problems/sort-colors/) problem could be easily solved with O(n) time and O(n) space by creating a new array and filling it up with the respective values in a sorted fashion. As an added challenge and space optimization, the interviewer will usually ask for an O(n) time and O(1) space solution which involves sorting the input array in-place.

An example of using the original array as a hash table is the [First Missing Positive](https://leetcode.com/problems/first-missing-positive) question. After the first for loop, all the values in the array are positive, and you can indicate presence of a number by negating the value at the index corresponding to the number. To indicate 4 is present, negate `nums[4]`.

##### 2. Change a data structure

[eg](https://www.techinterviewhandbook.org/coding-interview-techniques/#example-6)

You're given a list of strings and want to find how many of these strings start with a certain prefix. What's an efficient way to store the strings so that you can compute your answer quickly? A [Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) is a tree-like data structure that is very efficient for storing strings and also allows you to quickly compute how many strings start with a prefix.

## 4 Code out your solution while talking through it

- [ ] Only start coding after you have explained your approach and the interviewer has given you the green light.

- [ ] Explain what you are trying to achieve as you are coding / writing. Compare different coding approaches where relevant.

- [ ] Code / write at a reasonable speed so you can talk through it - but not too slow**-pace**

- [ ] Write actual compilable, working code **<u>where possible, not pseudocode</u>**

- [ ] Write clean, straightforward and neat code with **as few syntax errors / bugs as possible**.

- [ ] Use variable names that explain your code

  ```
  Good variable names are important because you need to explain your code to the interviewer. It's better to use long variable names that explain themselves. Let's say you need to find the multiples of 3 in an array of numbers. Name your results array multiplesOfThree instead of array/numbers.
  ```

- [ ] Ask for permission to **use trivial functions** without having to implement them
- [ ] Write in **a modular fashion**, going from higher-level functions and breaking them down into smaller helper functions
- [ ]  If you are cutting corners in your code, state that out loud to your interviewer and say **what you would do in a non-interview setting** (no time constraints).

Don’t do that ❌

1. Do not interrupt your interviewer when they are talking. Usually if they speak, they are trying to give you hints or steer you in the right direction.
2. Do not spend too much time writing comments
3. Do not repeat yourself
4. Do not use bad variable names
5. Do not copy and paste code without **checking** (e.g. some variables might need to be renamed after pasting)

## 5. After coding, check your code and add test cases

Once you are done coding, do not announce that you are done. Interviewers expect you to start scanning for mistakes and adding test cases to improve on your code.

- [ ] Scan through your code for mistakes - such as off-by-one errors
- [ ] Brainstorm **edge cases** with the interviewer and add additional test cases. (Refer to [algorithms cheatsheets](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/) for common **corner cases**)
- [ ]  Step through your code with those test cases
- [ ] Look out for places where you can refactor
- [ ]  Reiterate the time and space complexity of your code
- [ ]  Explain trade-offs and how the code / approach can be improved if given more time

❌ Don’t do that

1.  Do not argue with the interviewer. They may be wrong but that is very unlikely given that they are familiar with the question.

## 6. At the end of the interview, leave a good impression

- [ ] good questions
- [ ] THX

# After coding interview

- [ ] Record the interview questions and answers down as these can be useful for future reference
- [ ] Send a follow up email or Linkedin invitation to your interviewer(s) thanking them for their time and the opportunity to interview with them