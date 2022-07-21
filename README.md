# Timothy Johnson (Class Anemone) Capstone Project


# NAME: FearFuel

## Overview:
    A web app dedicated to the horror movies. Users will sign into an account to access a database of Horror movies. Specific titles will have detail pages including cover art, director, where to find them streaming. A user can add specific titles to personal "consumed" ("read" or "watched") lists, as well as tagging titles for a wish/watchlist. A private summary/review can be written so that a user may remember their favorite plots, quotes, and feelings about a specific title.

    As an avid fan of the Horror genre in all forms, I've seen a huge list of movies. I can't always remember what I've watched already, and would love a way to keep track. I imagine other fans of the genre would enjoy this platform as well; as of now it has no intentions of being another social network, instead acting as a private and personal log/journal tool.

## Tools:
    - Django Backend (Py)
    - Vue Frontend (HTML/JS)
    - Django Rest for User Lists (REST)
    - Framework (Tailwind? Skeleton?) + (CSS)
    - Custom User Model (
    - TheMovieDatabase API (AJAX/Axios)

## Features:
    
    - User account, profile, and lists.
    - Scraped databases of movies strictly within the horror genre.
    - Search specifics.
    - Favoriting/watchlists.
    - Personal summaries.
    - Recommended section.

## User Stories:

"As a Horror fan, I want to be able to log all the horror movies I've seen. I've seen so many I can hardly remember sometimes if I've already watched one." - J. Peele (Have-read/watched Lists)

"I don't just read horror literature, I consume it, ravenously. I love that FearFuel allows me to keep a curated list of what to read next."- M. Shelley (Read/Watch List)

"I know I've watched The Descent, but I can't really remember anything about it. At least I can check out the plot summary I wrote on FearFuel." - A. Bird (Private summaries/notes)

"I wish I knew which streaming app currently had movies in my watchlist. Oh wait, FearFuel shows me exactly which apps have that movie!" - K. Le (Streaming-On)

"Anne Rice has written a lot of books about vampires, I want to read them all! I'll search for her by name on FearFuel and add her books to my reading list." L. de Lioncourt (Search Specifics)

"I appreciate that FearFuel is not very cenetered around social media and sharing. For once a website feels like it's for ME." - T. Johnson (NOT another social app)

"I like ghost stories, but I think zombies are dumb, I'm going to search specifically for 'hauntings' as a subgenre on FearFuel." - G. Hastly (Subgenre filters)

"FearFuel is awesome, I hope they can implement horror videos games one day. Maybe even short stories!" - M. Haybie (Future implements)

## Data Model:

    USER -> PROFILE -> Name, Email, Password, Consumed(list), Marked(list)

    BOOKS -> Author, Title, Subgenre, Consumed(BOOL), Marked(BOOL), Notes(User text), PurchaseLink(URL)

    MOVIES -> Title, Director, Subgenre, Consumed(BOOL), Marked(BOOL), Notes (User text), StreamingOn(icon, maybe URL)


## Schedule:

    First Tuesday (7/19)
        - Proposal

    First Friday (7/22)
        - Django Project setup
        - API's Confirmed
        - Working index.html page
    
    Second Tuesday (7/26)
        - Database fully functional
        - User Profile page
        - User Lists Begin

    Second Friday (7/29)
        - User Lists functional
        - Recommended List
        - Styling, CSS Begin

    Third Tuesday (8/2)
        - Finishing Touches
        - Presentation Preparation

    Third Friday (8/5)
        - Present!

### Notes:

    - I should probably stick with one media type (e.g. Movies) to start off, unless by some magic I find an free public API that houses both movies and books.



