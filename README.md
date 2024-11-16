
# Git Commits to Jira  
 
Hey guys, so I decided to make a script that automates the process of adding each of your git commits as issues in your Jira with descriptions, and start/due date.

I want to eventually get it where it can detect who in the project contributed to what issue and fill in that field in Jira (still requires manual work). If someone would like to fork that feature to this repository, that would be really cool.

Nonetheless, here are the instructions.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file



`OPENAI_API_KEY` \
`GIT_REPOSITORY_PATH`\
`JIRA_SERVER` \
`JIRA_EMAIL` \
`JIRA_API_TOKEN` \
`JIRA_KEY`


Below are instructions on where you could find/get these environmental variables 

## OPENAI_API_KEY

The `OPENAI_API_KEY` is required to authenticate with OpenAI's API. This key allows the script to access OpenAI's services, such as generating text responses based on your prompts.

### Where to Find Your OpenAI API Key

To get your OpenAI API key:

1. **Log in to OpenAI**:
   - Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and log in with your OpenAI account.

2. **Create a New API Key**:
   - Click on **+ Create new secret key**.
   - Give your key a name if prompted, to help you remember its purpose (e.g., "Git Commits to Jira Script").

3. **Copy the Key**:
   - **Copy the API key** right away, as you won’t be able to view it again once you leave the page.
   - Store it securely, as it functions like a password for accessing OpenAI’s services.

4. **Set the Environment Variable**:
   - Add the key to your `.env` file or environment variables in the following format:

     ```plaintext
     OPENAI_API_KEY="your-openai-api-key-here"
     ```

### Example
Here’s how it might look in your `.env` file:

```plaintext
OPENAI_API_KEY="sk-abc123456789def098765ghi012jkl"
```

## REPOSITORY_PATH
This environment variable should be set to the path of your GitHub repository on your local computer. This allows the script to locate and work with your repository files.

### Option 1: Using GitHub Desktop
1. Open GitHub Desktop.
2. Select your repository from the list in the left sidebar.
3. Go to **Repository > Repository Settings**.
4. Under **Local Path**, copy the path shown.

### Option 2: Using the Command Line
1. Open a terminal (Command Prompt, PowerShell, or Terminal).
2. Navigate to your repository folder with `cd path/to/your/local/repository`.
3. Run `cd` on Windows or `pwd` on macOS/Linux to get the full path.

### Example
Set `REPOSITORY_PATH` to the full path of your local repository. For example:

```plaintext
GIT_REPOSITORY_PATH="C:/Users/yourusername/Documents/GitHub/your-repo"
```

## JIRA_SERVER
This environment variable should be set to the URL of your Jira server. Typically, this is the base URL for your Jira Cloud or Jira Server instance.

### Example
For a Jira Cloud instance hosted at `your-project.atlassian.net`, your `JIRA_SERVER` value would look like this:
```plaintext
JIRA_SERVER="https://your-project.atlassian.net/"
```

## JIRA_EMAIL
This environment variable should be set to the email address associated with the Jira account. Ensure that this account has the appropriate administrative rights or project permissions to create issues in the Jira project.

### Permissions Required
The Jira account associated with this email must have:
- **Create Issues** permission in the target Jira project.
- **Administrative or Project Lead permissions** if additional configurations or project settings are required by the script.

Without these permissions, the script will be unable to add issues to Jira, and you may receive permission errors.

### Example
For example, if your Jira account email is `your-email@outlook/gmail/etc.com`, set `JIRA_EMAIL` as follows:

```plaintext
JIRA_EMAIL="your-email@outlook/gmail/etc.com"
``` 
## JIRA_API_TOKEN

The `JIRA_API_TOKEN` is required to authenticate with Jira’s API securely. This token is used in combination with your Jira email to grant the script access to create and update issues in your Jira project.

### Where to Find or Generate Your Jira API Token

To generate a new API token:

1. **Log in to Jira**:
   - Go to [https://id.atlassian.com/manage/api-tokens](https://id.atlassian.com/manage/api-tokens) and log in with your Jira account.

2. **Generate a New Token**:
   - Click on **Create API token**.
   - Enter a label for the token (e.g., "Git Commits to Jira Script") to help you remember what it’s used for.

3. **Copy the Token**:
   - Once generated, **copy the token** immediately. For security reasons, you won’t be able to see it again after you leave the page.
   - Store this token in a secure location, as it functions like a password for your account.

4. **Set the Environment Variable**:
   - Add the token to your `.env` file or environment variables as follows:

     ```plaintext
     JIRA_API_TOKEN="your-api-token-here"
     ```

### Example
Here’s how it might look in your `.env` file:

```plaintext
JIRA_API_TOKEN="abc123def456gh789ijk012lmn345opq678rstuv"
```

## JIRA_KEY

The `JIRA_KEY` is the unique identifier for your Jira project. This key allows the script to know which project to add issues to when interacting with the Jira API.

### Where to Find Your Jira Project Key

1. **Go to Your Jira Project**:
   - Log in to Jira and navigate to the project where you want to create issues.

2. **Locate the Project Key**:
   - The project key is usually displayed at the top of the project’s main page, next to the project name. It typically consists of uppercase letters (e.g., `PROJ`, `TASKS`).
   - You can also find it in the project URL. For example, in the URL `https://your-project.atlassian.net/jira/software/projects/TASKS/boards/1`, the project key is `TASKS`.

3. **Set the Environment Variable**:
   - Add the project key to your `.env` file or environment variables in the following format:

     ```plaintext
     JIRA_KEY="your-project-key"
     ```

### Example
For example, if your project key is `TASKS`, set it in the `.env` file like this:

```plaintext
JIRA_KEY="TASKS"
```

## Additional Instructions
Please make sure your tasks have Start Date and Due Date fields. 

### How to Add Start Date and Due Date Fields in Jira Tasks

1. **Navigate to Project Settings**:
   - Open your Jira project and click on **Project settings** in the left-hand menu.

2. **Go to Issue Types**:
   - In the **Project settings**, select **Issue types**.

3. **Edit the Task Issue Type**:
   - Click on **Task** to edit its configuration.

4. **Drag and Drop Fields**:
   - On the right side, find the **Context fields** section.
   - Drag and drop **Start Date** and **Due Date** from the available fields list to the **Context fields** section.

5. **Save Changes**:
   - After making the changes, click **Save**. The Start Date and Due Date fields will now be available for tasks in your project.

## Message to UCF Senior Design and POOSD Teams
Hey, I know how tedious tracking commits and creating Jira issues can be, especially when you're juggling multiple tasks for senior design or POOSD. I feel your pain, and I hope this tool helps automate this process and makes your life a little easier. 🙂

P.S. If you want to tweak the output a bit, just modify the string in `prompt_text`. I'd recommend keeping the formatting instructions to ensure the output remains structured and easy to parse, but feel free to experiment!


