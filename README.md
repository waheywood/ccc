# Technical Annex

## Auction API endpoints

    1. GET
      * /api/auction/ List all available auctions.
      * /api/auction/{0} Get details for specific auction.
    2. POST
      * /api/auction/ Create a new auction.
      * /api/bid/ Create a bid on an auction. 

To create an auction you need the relevant data in the request.
    1. A description less than 255 characters.
    2. An end datetime in the format: YYYY-MM-DDTHH:mm:ss. 

The rest of the fields are generated from the request or from the user. 

To create a bid you need the relevant data in the request
    1. Auction ID 
    2. Bid amount

The rest of the fields are generated from the request or from the user. 

## Auth API endpoints

    1. POST
        */auth/token/ Gets a new token
        */auth/token/refresh Refreshes a token
        */auth/token/revoke Revokes a token
        */auth/register Registers a new user. 

## Tests 

Test cases cover the following: 
    1. Creation of a new user through the auth end points. 
    2. Getting a token from the oauth application
    3. Creating an auction.
    4. Bidding on an auction. 
    5. Listing all auctions
    6. Getting the details of a specific auction.
    7. Multiple bids on an auction. 
    8. Creating an auction in the past. 

## Future work

There are many ways that the site can be expanded for future. 

In terms of expansion to the site itself you could do the following: 

* Create categories for items so that users can search for specific categories of items to narrow down their selection if there are too many items. This could be done with either a built in category system or allowing users to "tag" items against which they can then be searched. 
* Allow for minimum bids. This would be done by setting a minimum integer difference between the present bid and the new bid. 
* Allow a bid up to option so that users do not constantly have to return to the site to check items. This would require the creation of a new table to monitor the maximum bid a person is willing to go up to on an item. When a new bid is placed this table is checked to see if it contains a higher bid and the highest of these bids is then used. 
* Create a notification system so people know when they have been outbid or a new item that matches their search criteria is added or they have won an item. This could be via e-mail or on the site itself. 
* Pictures for items. 
* An option to favourite or watch items to monitor them as they approach the end time. This would be done by creating a new table that is regularly checked for items approaching their end time so notifications can be sent to the intereseted users. 
* A messaging system to ask the item owners or the bidders questions. This could be via e-mail or an internal system. 
* A list of accepted payment methods on the items.
* A "similar items" list so that users can see items that are similar to the one they are presently looking at. This could look at items with a similar description, or if categorisation has been introduced via the intersection of the tags on the various items. 
* A "similar items recently sold for" marker on the auctions so people can see what other similar items have sold for. This would be similar to the above but with items that have recently expired. 
* Allow for reserve prices on items so they cannot sell for less than a certain amount. This would be an extra, optional field when creating an auction, if the bid is not above the reserve price at the end of the bidding then the item is not sold and the bidders would need to be notified. 
* "Wallet" feature. Allowing the users to credit a certain amount to their accounts that can then be used for bidding, this way the payment can be taken immediately from one users wallet and credited to the auction creators wallet. There would need to be a feature to allow for withdrawals from the wallet as well. 

There are additional expansion opportunities as well which are not related solely to the functionality of the site such as: 

* Adding two-factor authentication. This could be for when users log in or when they place a bid/create an auction.
* An option to reset passwords via an API endpoint. 
* The website could also have a HTML interface which takes advantage of the REST endpoints. 

