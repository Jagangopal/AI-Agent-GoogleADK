# AI-Agent-GoogleADK
**Projects**
  #1 my_first_agent -> first agentic ai project for basic understanding

**Installation and Execution**
  Step 1
  Create a virtual environment
  py -m venv .venv
  .venv\Scripts\activate.bat
  Note:
  Your prompt should now show (.venv) prefix.​

  step 2
  Install or reinstall the package:
  py -m pip install --upgrade google-adk
  Verify with py -m pip show google-adk​
  adk create my_first_agent

  step 3
  Execute the agent tool
  adk run my_first_agent

  step 4
  Access from Web 
  adk web --host 0.0.0.0 --port 8000
  http://localhost:8000
  Note:
  adk web -> defaults to 8000
