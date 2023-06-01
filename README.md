# Topic: Emotion dynamics in books related to technology
In this project, I try to analyze the top 8 books in the list from goodreads (https://www.goodreads.com/list/show/123917.Scary_Tech_Big_Data_Surveillance_Information_Overload_Tech_Addiction_Propaganda_Dark_Money_) Since the title of the book list is called "Scary Tech?: Big Data, Surveillance, Information Overload, Tech Addiction, Propaganda, Dark Money...", I wonder some emotion-related words can be commonly found in these books. 

The main project and results are included in the jupyter notebook called `final_project`, while another notebook `book_content_analysis` presents the process of how slowly built up these codes
In `book_content_analysis`, I started from processing a smaller e-book (sample1) to one whole book, following with some experiments with emotion words. 

For the list of emotion-related words, I use the NRC Emotion Lexicon, which is a list of English words and their associations with eight basic emotions: anger, fear, anticipation, trust, surprise, sadness, joy, and disgust. Source: http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm 
Reference: Mohammad, S. M., & Turney, P. D. (2013). Crowdsourcing a word–emotion association lexicon. Computational intelligence, 29(3), 436-465. 

All the e-books I use are in the file `books` and the plots for visualizing the results are in the file `plot`
