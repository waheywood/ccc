# Technical Annex

## API endpoints

    1. GET
      * /api/auction/ List all available auctions.
      * /api/auction/{0} Get details for specific auction.
    2. POST
      * /api/auction/ Create a new auction.
      * /api/bid/ Create a bid on an auction. 

To create an auction you need the relevant data in the request.
    1. A description less than 255 characters.
    2. An end datetime. 

The rest of the fields are generated from the request or from the user. 

To create a bid you need the relevant data in the request
    1. Auction ID 
    2. Bid amount

The rest of the fields are generated from the request or from the user. 

