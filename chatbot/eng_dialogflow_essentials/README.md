We got a request from a local store that runs a delivery service of food to create a chatbot to automate the delivery process.
They sent a list of features they want us to implement. 

Wishlist of features to be included in the chatbot: 
- new order: place new order, support payment through a chatbot
- track order: track order by order id, track order by phone number, track order by customer name
- offers/store hours: ongoing offers, upcoming offers, store hours

We start a negotiation with business team to set deadlines and feasible goals, as there are too many to begin with. 
To prioritize features is important to balance impact with feasibility. 
Business team tells us that the two most desirable feature are 'place new order' and 'track order by order id', so these will be our MVP (Minimum Viable Product) and we put them in our backlog in Jira, Asana or Notion. The rest of features will go into the backlog. 


When choosing a framework consider things like: 
- Time-to-market: how much time it will take to develop a first working solution. Prioritize frameworks that are quicker to implement.

We will be using Dialogflow as it's a cloud-based solution well-known for its good cost-performance relationship. It's been used by big companies such as Domino's Pizza, Ticketmaster, AirAsia or KLM.
There are two versions: Dialogflow Essentials and Dialogflow CX. The first is better for small or medium size projects whereas the other works better for larger models. 


Glossary:
Agent: equivalent for "chatbot"
Intent: the intention of the user (e.g. make a payment, start a new order, etc.)
Entities: values that can be taken as parameters (e.g. size, person, color, etc.)
Fulfillment: the reaction of the chatbot to the intents. 
Page: 