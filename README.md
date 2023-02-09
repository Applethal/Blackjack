# Blackjack
Blackjack decision making assistant

## 07/02/2023

Hello, a weekend ago I had some blackjack runs with a friend. Blackjack is the least luck based casino game I ever could play, as the consequences of your skills influence the output more than the luck factor.
Because I noticed a pattern in my decision making, and because a person that I care about wanted to try blackjack out; I decided to make this python code that would assist anyone, including myself in the future in case I forget the rules,
into maxing out the profit (provided the cards are not cheated of course.)
The decision making mechanism follows a logical algorithm that depends on some probability calculations. in the following paragraphs I will present the algorithm and further explain the ideas behind it.
As of today, the core of the code contains only the structure of the hand and some basic decision suggestions given to the player.
I highly recommend reading [this article, which further explains in detail the probability computation.](https://probability.infarom.ro/blackjack.html#:~:text=The%20total%20number%20of%20possible,of%20a%202%2Ddeck%20game.)

The article above recommends standing at 17, but I am more of a risk taker when it comes to such decisions and I would up things to 18, just because I like how the 8 looks like in comparison to 17.

I will be using the article's formula to determine the probabilities and through the comparisons, the script will suggest the next action. Note that I will simplify this problem to a case where only 1 deck is used, I might make an update where I allow custom decks, provided they all contain equal and fair number of cards.

$$P_{(x)} = \frac{4m - n_{(x)}{}}{52m-N} $$

m is the number of decks used in the blackjack game, while x is the card that you wish to obtain, n(x) expresses how many times the card has been dealt within the table and N is the total number of all the cards. 

Each deck contains 4 copies of the same card, making a full total of 52 cards per deck. This formula goes for any card other than 10, for the latter it would be 16 since the deck contains 4 ranks of the kingdom hiearchy cards, all of which net a value of 10, occupying roughly a third of the deck.


While I have no interesting music to share for today, [consider learning how to befriend spiders](https://www.youtube.com/watch?v=2uOA_ceFf4Q).
A good year ago I had the theory that the fear we humans have towards insects is generated from their legs, the rapid manouvering of their limbs creates an artificial feeling that makes us appreciate them less, what if insects never had legs ?


## 08/02/2023
I ran into some errands today and I came up super late that it prevented me from cooking more lines than how much I was supposed to do, but just to give away what I plan to do:
I simply plan to use a list for both the dealer and the player and loop over it to collect the sum of luck trafic using the formula above; next a comparison will process the decision making part of the code. 
while on my road, I ran some blackjack games and did encounter something odd that led me to a new discovery: A loss is issued whenever the players draws into 21 after a successful hit while the dealer has already obtained a blackjack. This is news to me yet it won't change anything in regards to the code. I am however disappointed since this shows how the luck factor is prioritied over the result of a decision. [Tidal wave came by while I was writing this readme](https://www.youtube.com/watch?v=VSwD_-kKcyI)

## 09/02/2023 

Small update that included the luck computation, it is not finished yet as it lacks the case where the dealer and the player share a given card. I lost my focus while trying to write the line that specifically adresses this.
![This is an image](https://pbs.twimg.com/media/FoKPb_YWQAMviGQ?format=jpg&name=small)

