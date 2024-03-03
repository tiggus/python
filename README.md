# car rental

Assessor to "role play" the following script:

"During this exercise I am going to play the part of a car rental firm owner. As the car rental firm owner, I don't know anything about technology, however I do know what I need. I have a set of requirements in the form of stories which we will implement one at a time. Once we're happy that a story is complete, we'll move onto the next story. We have quite a few stories, but the whole exercise will be capped at 1 hour.
This is not a race, we'll just get as far as we get in that time. You can ask me any questions you want about the requirements and scenarios. I will occasionally ask you questions about your solution (but not as the car rental owner), to help me understand your solution and or thinking. It is not important to implement all corner cases, however it is important to show there are things you might have considered if this was "production" code, and we can talk about those and decide whether to implement or not."


## Story 1 - finding a car to rent

As a car rental company I want to match a potential renter to a car that I have to rent...
...So that I can give a list of cars to a potential client.

acceptance criteria: one method returning a list of matching cars
design criteria: the method should be threadsafe (allowing it to be called from multiple threads)

## Story 2 - finding an available car to be rented

As a car renter I want to know if a car is available to be rented on the dates I need...
...So that i can provide a list of cars that are available on the dates given by the renter

acceptance criteria: the matching criteria for a renter to rent a car should include a from date and to date
acceptance criteria: the car renter should not be shown any cars that are booked in the period that is supplied
acceptance criteria: one method returning a list of matching cars (with the filter having changed) 
design criteria: the method should be threadsafe (allowing it to be called from multiple threads)

## Story 3 - booking a car

As a car renter I want to book a car which has been shown to me as being available...
...So that I can have a car available to me to use during the rental period

acceptance criteria: the car rental should be stored in an object model
acceptance criteria: there should not be able to have overlapping car rentals for the same car
acceptance criteria: two renters should not be able to book the same car at the same time for an overlapping period
acceptance criteria: one method allowing the car renter to book a car for a period
design criteria: the in memory storage should consider threadsafety, all access to and from it should therefore be threadsafe

Please see next page for more stories…
 

## Story 4 - car preparation

As a car rental company I need to understand what cars are coming up as new rentals on a specific date...
...So that I can make sure they are clean and ready to be rented

acceptance criteria: one method return all new rentals for the coming week ordered by date

acceptance criteria: the structure of the date returned should include the car model/make and it's registration as well as the date rented

## Story 5 - car maintenance

As a car renter i need to be able to make a car unavailable for rental for a specific period...
...So that I can make repairs to a car or get it serviced

acceptance criteria: the car being out of service needs to be booked like a car rental (but see below)
acceptance criteria: if the car to be booked already has an existing booking then I should be able to move the booking to a new car of the same alpha car rental group (if any exists) - for example a group "A" car
acceptance criteria: i should be able to differentiate between a rental and service booking
design criteria: during any booking movement we need to avoid another renters being able to book the car that the booking is moving to

## Story 6 - rental pricing

As a car rental company I want to show a blended price of all cars in the alpha part of the car rental group to a customer...
...So that I can manage individual car costs, but show a view at the group level

acceptance criteria: one method returning a list of matching cars which are available and which now includes a price
acceptance criteria: the booking method is updated to accept this new price which is stored alongside the booking information
=======
# python
