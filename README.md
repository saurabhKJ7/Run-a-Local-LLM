# Run a Local LLM with LM Studio

A simple Python script to interact with LM Studio's local LLM API.

## Setup

1. **Install and run LM Studio**
2. **Load a model (like Deepseek)**:
   - Go to Developer tab in LM Studio
   - Select your downloaded model (e.g., deepseek-r1-distill-qwen-7b)
   - Click "Load Model" (not just download)
   - Make sure it shows as "Loaded" 
3. **Start the local server** (default: http://127.0.0.1:1234)
4. **Install Python dependency:**
   ```
   pip install requests
   ```

## Usage

Run the script:
```
python simple_demo.py
```

## What it does

- Checks if LM Studio server is running
- Sends a prompt to your local LLM
- Gets the AI response  
- Prints: Prompt → AI → Response
- Shows helpful error messages if model isn't loaded

## Troubleshooting

If you see "No model loaded":
1. Open LM Studio
2. Go to Developer tab
3. Select a model and click "Load Model"
4. Wait for it to show "Loaded" status
5. Run the script again

## Files

- `simple_demo.py` - Main script
- `requirements.txt` - Dependencies

That's it! Simple local LLM interaction.