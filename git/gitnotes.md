# Git Notes

##Keynotes

- Github and Bitbucket (from Atlassian) can have different flows for git
  - **Github:** clone from shared, new branch, push new branch to shared, pull request for branch
  - **Bitbucket:** fork from shared, clone, develop, commit, push to personal, pull request to shared


### Github Flow:
git clone
git checkout -b <new-branch-name>

git pull origin master (or <new-branch-name>)
git status

git diff - see file difference in terminal
gitk - see difference in GUI

git add .
git commit - be explicit with commit message for PagerDuty

git push origin <new-branch-name>


git stash = save last commit
git merge = merge branches with merge conflict
git checkout = grab file from master or whatever
git reset = unstage changes for file (after git add)


