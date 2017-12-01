# Interview Project - Backend

### Project 
Statement:
Build an API to display data related to a given location. For example: if the user enters New
York, we would like to get results from Yelp, Uber, Foursquare etc for the given location.

#### Module 1:

**Task -** Build an API which fetches data from multiple APIs and store the results in the database. 

**APIs** : Uber, Yelp, Foursquare <br>
**Input** : `location`<br>
**Output** : Boolean flag - data saved in DB or not?<br>
<br>
**Example** :`api.test.com/save?location=London`<br>
**Output** : `{“saved”:true}`<br>
<br>
**Action Item** - Deploy this API on AWS cloud (or any cloud operator) and share the url <br>
<br>
#### Module 2:

**Task -** Build an API which fetches data from the database (data which was stored via Module 1), transforms it in the right format and return it in JSON format.<br>

**Input** : `location`<br>
**Output** : `json` result<br>
<br>
**Example** :`api.test.com/fetch?location=London`<br>
**Output** : `json` result <br>
<br>
**Action Item** - Deploy this API on AWS cloud (or any cloud operator) and share the url <br>

#### General Guidelines:


- Feel free to use any tech stack - any language that you are comfortable with and any
database.
- Project will be evaluated based on code quality, database design and project comple-
tion within time limit.
- Push the code in the repository (GitHub or any other) and deploy your code on the
cloud. If you haven't pushed any code on AWS etc., please ask for the details. 
- Although we prefer optimized code but don't put too much focus on optimization/
performance of the code for this project.
- Although the features of module 1 and module 2 API can be combined into one API,
we have deliberately kept them separate. 


