# Enodo Fullstack Engineering Challenge

Welcome to our Fullstack Engineering Challenge repository. This README will guide you on how to participate in this challenge.

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.


## Challenge


Front-end and backend to allow users to search, select, or unselect properties from the DB.

## Requirements
- Build frontend with Element.js and Vue.js
- Create DB from data in excel file (suggestion: Sqlite)
- Create API to interact with database (suggestion: falcon, flask, express...)
- Input field with [autocomplete](https://element.eleme.io/#/en-US/component/input#autocomplete), displaying the properties from the DB through the API.
  - On Selection of search result, save as "Selected" to DB.
- Table Showing selected properties:
  - Column 1: Full Address
  - Column 2: Class Description
  - Column 3: Delete button
- Include a delete button to unselect property from DB.
- Add a test to your implementation.
- Include a Readme on how to run your solution.

---

## Install, Test and Run

### Install

```
git clone git@github.com:saintsGrad15/enodo-fullstack-challenge.git

cd enodo-fullstack-challenge

virtualenv --python=python3 enodoenv
source enodoenv/bin/activate

pip install -r requirements.txt
```

### Test
```
# Please run with the root of the repo as your working directory
python3 tests/test.py
```

### Run
```
python3 run.py
```

## Shameless Pandering

Thank you for the opportunity to demonstrate my knowledge and skills.

I look forward to speaking with the Enodo team soon!
