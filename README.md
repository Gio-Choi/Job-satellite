## CBF Recommendation System for Job/Job Posting for IT Job Seekers (January 2021)
### Awarded Second Prize in Big Data Specialization Final Project at the ‘SW Basic Competency Academy’ organized by Seoul Business Agency and Asia Economy

### Project Overview
We developed a service where job seekers can input their skills (e.g., Java, C++) and receive recommendations for:

1) Jobs and 2) Job postings suitable for the skills of applicants.

Additionally, if they input their values (e.g., work-life balance, benefits), the top 5 recommended jobs and postings will be reordered based on those values.

#### 1. Data Collection
   1) Source: Jobplanet  
      a) 1882 job postings for IT positions as of January 25, 2021
      b) Evaluation data (values) from IT company employees 
   2) Collection Method: 
      • Crawling (using Selenium library)

#### 2. Preprocessing (Technology Terminology Dictionary)
      1) Necessity
      Before implementing the recommendation system, we needed a standardized dictionary of technical terms categorized by job roles to extract the required skills for each job. 
      Therefore, we created a technology dictionary based on the crawled job postings. Using this dictionary, we extracted job-skill matrices and job posting-skill matrices. These two matrices were then compared with the skills inputted by users using cosine similarity in the recommendation system.
      2) Dictionary Creation Process
      • Set preprocessing rules (excluding suffixes, particles, special characters/extracting specific pattern words)
      • Developed functions for preprocessing rules and extracting similar words
      • Added stopwords after reviewing the results
      • Extracted only words that appeared more than 35 times
           
#### 3. Implementation of Job/Job Posting Recommendation System
      • Used the `CountVectorizer()` function from the Sklearn package to extract:
        - An 18 jobs-70 skills matrix
        - A 1882 postings-70 skills matrix     
      • Measured the similarity between the user's inputted skills and the skills in these two matrices using Cosine_Similarity()
      • Recommended 5 jobs and 5 postings, then reordered the final recommended postings based on values (Jobplanet company evaluation data).
   
#### 4. Expected Benefits
   IT job seekers can focus and make better choices by using the recommended jobs/postings.
