# Python BlackJack Version
## Overview
As part of [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code), Day 11 involved creating a Blackjack game in text mode. That was the beginning of this code. By the time learning about classes came up, I'd been studying PyGame on the side, and I revisited the original Blackjack and made it graphical.

<img src="https://github.com/mdanielskeys/PyBlackjack/assets/12840668/00c2ebc5-c5a8-434c-b740-599636547c36" width="300" />


## Learning
I tried to separate my logic from my display and avoid repeating myself in the code. I also tried to minimize the dependencies, which involves using dynamically typed language since it is pretty easy to do. However, the design could move to a statically typed language with interfaces quickly.
## Tools
This was built in PyCharm. I've grown to like the editor. The only external dependency is pygame.
## Next Steps
The game implements a subset of blackjack's rules. It needs some additions and perhaps some study to be complete.
### Betting
Add a betting component. Start the player with a bank, allow them to adjust their bet, and keep track of the winnings or losses.
### Additional Rules
Allow the player to Split and Double down when the situation calls for it. This will test the flexibility of my class states and how easy or hard it is to insert a new state.
### Remove Text Mode
I still have text mode pieces in place that play in the background. They do no hard, but are not necessary. Perhaps I'll make them a command line option for debugging purposes.
