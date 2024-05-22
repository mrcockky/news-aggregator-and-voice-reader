## Project Description

Developed a Python application that aggregates the latest news articles from BBC News and reads them aloud using text-to-speech technology. The application leverages the NewsAPI to fetch top news articles and utilizes the `win32com.client` library to convert the text to speech, providing users with an accessible way to stay updated with current events.

## Objectives

1.  **News Aggregation:** Fetch the latest news articles from a reliable source.
2.  **Text-to-Speech Conversion:** Read out the news articles for user convenience.
3.  **User-Friendly:** Ensure the application is easy to use and provides quick access to trending news.

## Solution

To achieve these objectives, the application was designed with the following components:

-   **NewsAPI Integration:** Using the [`newsapi`](https://newsapi.org/docs/client-libraries/python) library, the application fetches top news articles from BBC News.
-   **HTTP Requests:** The [`requests`](https://requests.readthedocs.io/) library handles HTTP requests to the NewsAPI, ensuring smooth data retrieval.
-   **Text-to-Speech Conversion:** Utilizing the `win32com.client` library, the application reads out the news headlines, making it accessible for users who prefer audio content. you can choose other tts module as well according to your needs.

## Impact

-   **Convenience:** Users can listen to the latest news headlines, making it easier to stay informed while multitasking.
-   **Accessibility:** The application caters to users with visual impairments or those who prefer auditory content.
-   **Efficiency:** Fetches and reads news headlines quickly, providing a streamlined user experience.

## Technologies Used

-   **Programming Language:** Python
-   **APIs:** [NewsAPI](https://newsapi.org)
-   **Libraries:** [requests](https://requests.readthedocs.io/), win32com.client (Dispatch)
-   **Tools:** [PyCharm](https://www.jetbrains.com/pycharm/), Command Prompt

## Skills and Deliverables

**Skills:**

-   API Integration
-   HTTP Requests Handling
-   Text-to-Speech Implementation
-   Python Scripting

**Deliverables:**

-   Python script for news aggregation and text-to-speech conversion
-   Documentation for setting up and running the script
-   Source code with comments for clarity and maintainability

## Code Example
    from newsapi import NewsApiClient
    import requests
    from win32com.client import Dispatch
     #Initialization
    newsapi = NewsApiClient(api_key='YOUR_API_KEY')
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "YOUR_API_KEY"
    }
    main_url = 'https://newsapi.org/v1/articles'
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    
     #Getting all articles in a string article
    article = open_bbc_page["articles"]
    
    #Empty list which will contain all trending news
    results = []
    
    for ar in article:
        results.append(ar["title"])
    
    for i in range(len(results)):
        # Printing all trending news
        print(i + 1, results[i])
    
    #To read the news out loud for us
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)` 

## Instructions for Running the Script

1.  **Install Required Libraries:**
   `pip install newsapi-python`
   `pip install requests`
  
2.  **Set Up API Key:** Replace `'YOUR_API_KEY'` with your actual NewsAPI key in the script.
3.  **Run the Script:** Execute the script in your preferred Python environment.

## Conclusion

The News Aggregator and Voice Reader application effectively combines news aggregation and text-to-speech technology to provide a user-friendly experience for staying updated with current events. This project demonstrates my ability to integrate APIs and implement text-to-speech functionality in a Python application.

