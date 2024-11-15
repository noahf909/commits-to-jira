import os
import json
from openai import OpenAI
from git import Repo
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

# Set up OpenAI API client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the Git repository
repo = Repo(os.getenv("GIT_REPOSITORY_PATH"))


# Extract commit data
commits = []
for commit in repo.iter_commits():
    commit_info = f"Date: {commit.committed_datetime}, Author: {commit.author.name}, Summary: {commit.summary}"
    commits.append(commit_info)



# Prepare the text prompt for GPT API
prompt_text = (
    "The following is a list of commit events. Generate a long, extensive timeline of the main events and subevents."
    "with starting date-finish date, collaborators who worked on them, and a brief description of why the commit was done. "
    "Provide the output in the following structured JSON format:\n\n"
    "{\n"
    "  \"events\": [\n"
    "    {\n"
    "      \"event\": \"Event Name\",\n"
    "      \"start\": \"YYYY-MM-DD\",\n"
    "      \"end\": \"YYYY-MM-DD\",\n"
    "      \"collaborators\": [\"Collaborator 1\", \"Collaborator 2\"],\n"
    "      \"description\": \"Brief description.\"\n"
    "    },\n"
    "    ...\n"
    "  ]\n"
    "}\n\n"
    + "\n".join(commits)
)



# Use the GPT API to generate the timeline
try:
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt_text}],
        model="gpt-4"
    )
    timeline = chat_completion.choices[0].message.content
except Exception as e:
    print(f"Error with GPT API call: {e}")
    timeline = "{}"

# Save to a file (optional)
with open("commit_timeline_summary.txt", "w") as file:
    file.write(timeline)

# Parse GPT output
try:
    timeline_data = json.loads(timeline)
    events = timeline_data["events"]
except json.JSONDecodeError as e:
    print(f"Error decoding GPT output as JSON: {e}")
    events = []


# Connect to Jira
jira = JIRA(
    server=os.getenv("JIRA_SERVER"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

# see JIRA fields
'''
fields = jira.fields()
for field in fields:
    print(f"Name: {field['name']}, ID: {field['id']}")
'''

# Create Jira issues from parsed events
for event in events:
    try:
        issue_fields = {
            "project": {"key": "MERN"},  # Replace with your actual project key
            "summary": event["event"],
            "description": f"{event['description']}\nCollaborators: {', '.join(event['collaborators'])}",
            "issuetype": {"name": "Task"},
            "duedate": event["end"],                # Due Date (use in YYYY-MM-DD format)
            "customfield_10015": event["start"]     # Start Date (use in YYYY-MM-DD format)
    }
        new_issue = jira.create_issue(fields=issue_fields)
        print(f"Created issue {new_issue.key} with summary: {issue_fields['summary']}")
    except Exception as e:
        print(f"Error creating Jira issue for event {event['event']}: {e}")