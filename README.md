# Blackjack
Blackjack decision making assistant. *Casinos shall hate you starting from today!*
<details>
  <summary>Click me for the a report on how things went when making this program</summary>

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


![This is an image that I fascinated about today.](https://pbs.twimg.com/media/FoKPb_YWQAMviGQ?format=jpg&name=small)


## 11/02/2023 
Today is the day!
Fixed some issues, coded the execution. Apparently there will be more fixes to come, hopefully I will be able to fix them all by tomorrow, afterwards this readme file will get polished. I still need to fix an issue where the opponent always gets a hand value of 20, making the program advising you always against hitting unless you hit a blackjack of course, which is a very rare occurance. I always thought that I would be able to do all of this within one full day, though I am super happy with the results, I hated how I had to borrow the formula from an article instead of coming up with my own and the fact that I have spent only up to 20 minutes aprox. every day instead of hyper focusing, but that got me thinking: why not design a GUI for this ? Sure, once I learn how to manage it!
While doing all of this [Jiro Inagaki 's music came along on spotify, I can safetly recommend it to anyone!](https://www.youtube.com/watch?v=kjxxVkSd0XA)
  
## 12/02/2023
All lines fixed! the program is ready to be used by anyone, I am happy to announce this. Just one small change though: I made it so that the calculation assumes that the dealer always has a 7, I ran about 50 games and on average the dealer had 10's, 8's and 7's and I decided to go for the 8th to balance the numbers and compensate the decision making part.
  
</details>

Blackjack is a card based game where the goal of each player is to obtain a hand of cards with a total value that excceeds everyone else's hands while also be on the edge of a value totalling to 21. Each player starts with 2 cards and is given the option to either obtain a new card or to express their current satisfaction by holding.
The classic blackjack deck contains the following cards:

![Source:pngwing com](https://user-images.githubusercontent.com/114657050/218333201-27716d2f-aeb4-4b25-bfd6-aa246c653ded.png)

Each card has 4 copies, their values match the number shown on them, while the ace card mirrors a doublette of +1 and +11. There are 16 cards that can net the player a 10, making it a case that about at least once each 3 runs. Using the formulas from [Catalin Barboianu's book](https://www.amazon.de/-/en/Catalin-Barboianu/dp/9738752035) I made this python script that allows the user in some specific cases to decide on whether a hit or hold should be processed after performing a luck calculation comparison between the dealer and their hand. Because the dealer's second card is never shown, it will be assumed that he has a card whose value starts from 8. Although there are lots of strategies when it comes to playing in an optimal manner, most of them depend on the coins/money parameter, which is absent in this project. Maybe an update will happen where I incorporate these.

# How to use the program ?
Just run it and follow its instructions, of course python should be installed on your windows machine, that is all what you need. The luck comparison simply sums up over the chance of all the cards required for you to get closer to 21 and compares it with the dealer's chance, then if the chances of busting are low, a hit will be suggested.

## What's next ? 
Fixing the things that I have overlooked, for that I would require more tests and eventually an issues report by anyone who comes across the issues, you know what to do!
I aim to also consider learning how to make a UI just to design one for this program. While writing this paragraph,[Wishing Ain't No Sin by Billy Momo came up on my music player.](https://www.youtube.com/watch?v=S2-kas5e_vU) I am proud of how this went at the end, it took one week to build all of this.




