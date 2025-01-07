import os
import pandas as pd


file_path = "./masterships - Uni.csv"

scholarships_df = pd.read_csv(file_path)


def create_markdown(row):

    template = f"""
# {row['Name']}

**Author: [ YOUR_NAME] **

| **Field**                  | **Details**                                                             |
|----------------------------|-------------------------------------------------------------------------|
| **URL**                    | {row['URL']}                                                            |
| **Country**                |                                                                         |
| **University Ranking**     |                                                                         |
| **Program Quality**        |                                                                         |
| **Program Duration**       |                                                                         |
| **Stipend**                |                                                                         |
| **Application Deadline**   |                                                                         |
| **Living Costs Estimate**  |                                                                         |

---

## Scholarship Overview

[Provide a brief description of the scholarship and its key objectives.]

---

## Academic and Language Information

- **Program Requirements**: [List GPA, test scores, or other academic criteria.]
- **Studying Language**:
  - **Proficiency Required**: [Indicate required language proficiency levels.]
  - **If Not Proficient**: [Explain options if the applicant doesn't meet language requirements.]
- **Additional Language Support**: [Specify if the program offers preparatory courses or resources.]

---

## Coverage and Conditions

- **Scholarship Coverage**:
  - [ ] Tuition
  - [ ] Housing
  - [ ] Health Insurance
  - [ ] Travel Costs
  - [ ] Living Expenses
- **Scholarship Conditions**: [List conditions like maintaining a specific GPA, work restrictions, etc.]

---

## Required Documents

[List all documents needed, such as transcripts, recommendation letters, proof of language proficiency, etc.]

- [Document 1]
- [Document 2]
- [Document 3]
- [Document 4]

---

## Application Process

[Provide a step-by-step guide for applying, including online portals, interview requirements, etc.]

1. [Step 1: Description]
2. [Step 2: Description]
3. [Step 3: Description]
4. [Step 4: Description]
---

## Eligibility Criteria

[Specify criteria like nationality, field of study, age limits, etc.]

- Nationality: [Eligible Nationalities]
- Field of Study: [Eligible Fields]
- Age Limits: [Age Limits]
---

## Fields Available


[List of Available Fields]
---

## Notes

[Add any special notes, like tips for application success or unique features of the scholarship.]

"""

    return template


output_dir = "scholarship_markdowns/"

os.makedirs(output_dir, exist_ok=True)


for _, row in scholarships_df.iterrows():

    if pd.notnull(row['Name']) and pd.notnull(row['URL']):

        markdown_content = create_markdown(row)

        filename = f"{row['Name'].replace(' ', '_').replace('/', '_')}.md"

        file_path = os.path.join(output_dir, filename)

        with open(file_path, "w") as file:

            file.write(markdown_content)
