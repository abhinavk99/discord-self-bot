# self-bot

Discord self bot written in Python. Meant for user accounts to use for utility functions.

You'll need a file called `config.py`. In it, copy paste the below:

```python
TOKEN = 'token' # put your actual user token in the quotes
```

## Commands

| Command | Description | Usage | Example |
| --- | --- | --- | --- |
| -delete | Delete past n number of messages by the user | -delete `<number>` | `-delete 7` |
| -edit | Edit the last message by the user with new text | -edit `<new content>` | `-edit Hi, I'm SelfBot.` |
