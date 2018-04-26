# Agile Notes

## Agile Manifesto

### Individuals and Interactions > Processes and Tools
- processes and tools help but it's individuals and interactions that will make Agile work
- Agile Culture and Structure needs to be followed; processes and tools jsut help on the side

### Working Software > Comprehensive Documentation
- code should work so intuitvely, documentation shouldn't even be needed

### Customer Collaboration > Contract Negotiation
- collaboration is more productive than arguing over contract

### Responding to Change > Following Plan
- there could be huge errors in estimating the project scope; better to start than plan too far ahead

## Empirical Process Control
### Scrum Theory
**Transparency:** on same page between developer and product developer
**Inspection:** analyze the sprint health status 
**Adaptation:** based on inspection, make changes to sprint

## Backlog Refinement
Why?

- very important for reducing risk and understanding scale of task
- good to have a few days between refinement to Sprint Planning

Product Owner:

- recommend product owner to email list of stories/tasks a few hours before refinement
- end meeting as soon as selected items have been refined for motivation boost

Goals: 
- talk about AC, in/out of scope, dependencies, target date

Meeting:
- 1 hour per week is recommended
- If sprint planning is too long, then we need more refinement is needed

## Sprint Planning
- Close next sprint and carry over work from last sprint
- Assume carry-over work as 'from-the-beginning' (takes time to get caught up)
- Determine story point budget (use rolling historical average or last sprint's points)
- Have 1.5 to 2 sprints' worth of Ready stories
- Fist of 5 to determine confidence of next sprint
- Create a sprint goal (purpose of the work)
	- not all backlog stories have to relate to sprint goal
- Report what we want to accomplish next sprint
- Should take 2-4 hours

## Daily Standup
**Not a status report for project owner / manager**

- To discuss how their sprint is going
- Course correction
- We want "physical huddling", not everyone report to one person

What it Should Involve:

- Same time every day + start meeting on time
- Task board + burn down chart
- 3 Questions for Each Member
  - What did I do yesterday to help the sprint goal?
  - What will I do today to help sprint goal?
  - Do I see any impediment from meeting the sprint goal?
- Discussions that does not need everyone present can be put **on hold** for meeting after daily stand up
- Answer the question: **Can we meet our goal and finish the sprint backlog?**
  - Should we change the course of action? Should we remove a sprint backlog item?

## Sprint Review
- show results from end user perspective, not code
- demonstrating in staging is fine (does not need to be production)
- good to get feedback from stakeholders
- product owner shares updates
  - What is the current state of the backlog?
  - Have any long-term forecasts/goals changed?
- adaptation for future sprint (external events, priority shifts)

## Sprint Retrospective

- Meta note: one of the most important events in scrum
- After sprint, major event, major incident
- Create experiments with different flows for the team
- Vary retrospectives to make it interesting

### 5 Steps of Retrospectives

1. Set the stage (2 of the below activies)
  - Read as a team: "Regardless of what we discover, we understand and truly belive that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand. - Norm Kerth
  - 1 Word to describe their feeling for sprint
  - Voice specific appreciation for another member of the team

2. Gather Data
  - List out positives, deltas (changes), insights under a timebox
  - Group similar items together

3. Generate Insights
  - Choose top positives/deltas/insights
  - Find root causes (5 Whys?)
    	- If you are not surprised by the insight, then it's most likely not the root cause

4. Decisions and Actions
  - How to persist the positives, change/minimize deltas, capitalize on insights
  - Two Categories: decisions (changes to working agreement) and actions (new backlog items)
  - We want 1-3 items to focus on changing, not too much

5. Wrap Up
  - Retrospect on the retrospective

### Example Retro Using Trello

1. Actions (from last retro)
- One Word Description of Sprint
  - Each team member explains their word choice
- Appreciations
- To Discuss
  - vote the most important discussion points
- Discussing
- Done
- Action Items

## Definition of Done
- **"Did the Thing Right"** as opposed to acceptance criteria - "Did the Right Thing"
- Team definition of acceptable quality
- Decreases technical debt and production bugs in long run

Example Definitions:

- Code complete
- Unit/Integration and Performance Tests
- Light documentation
- No new bugs or tech debt
- Accepted by PO/PM with accordance to acceptance criteria
- Review it in Sprint Retro'

- Explain in PR how AC is met (what it does, testing, pictures)

## Definition of Ready
(ready to work on)
- think of it similar to cooking shows where the chefs have measured and prepared all their ingredients

U - I.N.V.E.S.T.

User Experience - Determine acceptable UX, perhaps get UX designers to work on it first before dev work
Independent - No dependency on another item in same sprint
Negotiable - Discuss scope and AC of item
Valuable - Must deliver value to its stakeholders
Estimable - Must be able to estimate size of story
Small - Ideally, a backlog item should not take more than half the sprint to complete
Testable

## Working Rules
Examples:

1. No Computers
  - Problem: People are on computers during meetings
  - Impact: Team is not productive during the meeting
  - Solution: Only speakers can have computer
  - Solution: People working on production issues need to leave the meeting

## Vertical and Horizontal Slicing
**MOST IMPORTANT ASPECT OF AGILE THINKING**

**Epic:** Stories that cannot be completed in one sprint
- allows for iterative feedback from stakeholders as the product comes to fruition
- easier to gauge progress

Right Way: Vertical Slicing
Wrong Way: Horizontal Slicing

Example: People want vertical slice of cake, not a horizontal slice

Software Layers:
- Presentation
- Application
- Business
- Data Access
- Infrastracture

Doing each layer at a time will miss out on **early exposture** and **valuable feedback**

Vertical work does create throwaway code, but it's easier to adapt and less risky

## User Story
### 3 C's of User Story
1. Card
  - Physical token related to the story (or JIRA)

  a. Title
  
    - As a [persona], I can [goal/task], so that [value]
    - Persona should mostly be end user

  b. Acceptance Criteria
  
    - List of user expectations or non-functional requirements
    - Alternatively, can also use *gherkin*
      - GIVEN [context], WHEN [something happens], THEN [observable consequence]

  c. Out of Scope
  
  d. Dependencies (blocked by, blocks)
  
  e. Notes/Mocks/Diagrams
  
  f. Story Estimate
  
2. Conversation
  - Negotiate story
  - Scrutinize solution
  - Quantify qualitative descriptions

3. Confirmation
  - AC agreed by both sides
  - Go through ACs with PM/PO at the end to verify completion

## Story Pointing
- 1 point = Least complex, most certain, lowest effort
- Rate based on **CUE:** **complexity**, **uncertainty**, and **effort**
- Use Fibonacci sequence to give a considerable difference between points (compared to 9 vs 10)
- More accurate and easier to guess than time-based estimates

### Planning Poker
- for smaller backlog
- benefits most from having "reference point" stories
- discuss each item throughly
- vote using cards with points
- if points are drastically different, ask minority or the lowest/highest points
- vote until everyone agrees

### Affinity Estimation
- rapid estimation
- good for new team, new backlog, or release planning

How-To:
- one backlog item per sticky note
- if possible, add some previously-estimated stories and put their points up
- create a spectrum from **"Least CUE"** to **"Most CUE"**
- Try doing it in silence
- Discuss ordering of stories at the end
- Put in previously-estimated stories on the spectrum and use them as reference to assign points to the new stories

Estimate 1 Quarter of Work = 3 hours

## Scrum Team
- each team should not have to rely on another team
- team should be close and layout should encourage collaboration
- no specific titles
- focus on 1 project (20% loss of productivity per project due to context switching)
- 3-9 developers per team

### Product Owner
- maximizing value of product made by dev team
- manages product backlog (ie. prioritization)
- connect customers with dev team

PO Responsibility:

- What
- Why
- Relatively When

Team Responsibility:

- Absolutely When
- How

Time Split (1/4 total time):
- Talking to customers/stakeholders
- Developing/communicating the vision/roadmap/product backlog
- Research/Analysis
- Speaking with team

### Scrum Master
- clarify goals with team
- ensure backlog items are defined
- ensure team knows why
- facilitate events such as Sprint Retro
- encouraging pairing/swarming on important items

### Engineering Manager
- an agile engineering manager is more for team support; only use authority to protect relationship between team and company and company and stakeholders

1. keep team aligned with business objective
  - create expectations
  - update team on progress
  - align with company values
2. Team Productivity
  - monitor and identify team's needs
  - resolve conflicts
  - hire team members that will fit the team
  - focus on inclusive environment
3. Individual Productivity
  - help team members improve their skills
  - clarify plans/outcomes/expectations
  - conduct performance evaluations
4. Administrative


## Agile Principles
1. Highest priority is to satisfy customer through early and continue delivery of software
  - Waste: anything customer doesn't want or isn't willing to pay for
2. Welcome changing requirements, even late in development.
3. Deliver iterations of working software as soon as possible
4. Business people and developers must work on the project daily
  - clarify goals and remove impediments
5. Build projects around motivated individuals
  - 3 things that motivate us the most: autonomy (individuality), mastery, purpose
  - **don't micro-manage**
6. Most effective method of conveying info is vis-a-vis conversation
7. Working software is the primary measure of progress
  - no working software = no value for customers
8. Agile processes promote sustainable development (constant pace; no excessive effort)
9. Continuous attention to technical excellence and good design
  - need code base maintainable and easy to work with
10. Simplicity is essential
  - maximize the amount of work not done (but getting rid of unnecessary work)
11. Best architectures, requirements and designs come from self-organizing teams
  - as opposed to having 1 architect who will standardize across company
  - focuses on investing in employees
12. Reflect on team's effectiveness at regular intervals and make improvments