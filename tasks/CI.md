## Continuous Integration Task

The goal of this activity is for you to configure continuous integration using Github Actions.

## Step 1: Make sure you can run tests locally

Double check that you can run the tests following the README instructions. 

## Step 2: Add a basic workflow file

Your tests run locally, but let's make them run with every push to your repo! You will need to create a new workflow file under the location (`.github/workflows/<workflow name>.yml`).

Let's call the file `test.yml` and create the workflow such that it gets triggered with every push to the main branch.


```
name: Run tests

on:
    push:
      branches:
        - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        
	# your task: figure out the remainings steps 
	# that match your selected language. 
	# Hint: follow slide 11 for inspiration
	# You should first find an action that sets up the environment
	# for your selected programming language. 
	# You should then set up the steps to run similar to how you run
	# them locally
```

Commit and push your new yaml file. You should see a CI build being triggered. Check out its details to understand what's happening.

## Step 3: Make the build fail

Just for fun, introduce a syntax error or make one of the tests fail and then commit and push and watch the CI build status change to a failed build.

Fix the problem and commit and push again and make sure you now see a green check mark.

## Step 4: Make the build also get triggered on PRs

Change your workflow file to also trigger the build on pull requests, rather than just a push to main. Check the [docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) and figure out what you need to change.

Commit and push the changes you made to the workflow file.

Well, you need to believe it actually worked so perhaps just create a test branch and PR and check that the CI build got triggered when you opened the PR.

## Step 5: Differentiate what happens in pushes to main vs. PRs

Assume you want to run some additional checks on PRs that give you confidence about the proposed change. For example, you run some style checking tool on the PRs. Change your workflow file to do different things for a check on a push to the main branch vs. a check on a PR.

## Step 6: Calculate coverage during CI builds and include a ReadMe badge

Ok, so now you want to make sure coverage is calculated and displayed during CI builds. 

For inspiration,check this [available action](https://github.com/cicirello/jacoco-badge-generator) on how to update your workflow file to do that for Java. Find similar actions that help you.


## Step 7: Run on multiple Python versions

We all know how different versions of language runtimes, libraries, frameworks (you name it!) can mess things up. Let's make sure that our code builds and runs on multiple recent Python versions.

Update your workflow file to use a matrix build to run things on multiple Python versions. For inspiration, see [https://github.com/actions/setup-java](https://github.com/actions/setup-java) for documentation on how to test against multiple java versions.

Don't forget to test it with a push and/or PR (depending on which workflow you modified).
