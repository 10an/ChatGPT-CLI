# ChatGPT-CLI

A _very_ minimal terminal interface for OpenAI's API - Written in Python

## Requirements

To use ChatGPT-CLI, you need to meet the following requirements:

- An OpenAI API key set as an environment variable. To set the API key, follow the instructions specific to your operating system:

  - Windows:
    - Open a command prompt and run the following command:

      ``` powershell
      setx OPENAI_API_KEY "<API-Key>"
      ```

    - Replace `<API-Key>` with your actual OpenAI API key.

  - Linux:
    - Open a terminal and run the following command:

      ``` bash
      echo "export OPENAI_API_KEY='<API-Key>'" >> ~/.bashrc
      ```

    - Replace `<API-Key>` with your actual OpenAI API key.
    - Restart the terminal or run `source ~/.bashrc` to apply the changes.

- A terminal emulator with support for ASCII colors.
<!-- - `flask` package -->

## Install needed packages

``` python
pip install openai flask
```

## Usage

Follow these steps:

1. Download the ChatGPT-CLI source code from the repository.
2. Open a terminal and navigate to the directory containing the source code.
3. Run the cli.py script using the following command:

    ``` bash
    python cli.py
    ```

4. Be imaginative

_Note: You can change system prompts and max chats from inside the script._
