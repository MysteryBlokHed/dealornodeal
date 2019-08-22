# Deal Or No Deal!
This is a Python console app that simulates the game show(s) [Deal Or No Deal](https://en.wikipedia.org/wiki/Deal_or_No_Deal).

## Requirements
**Python v3.6+**  
If you don't already have it, download it [here](https://www.python.org/downloads/).

## Starting the game
To start the game, just change directory to the one with `__main__.py`, and run `python __main__.py`.

## Customize the game
I have a few variables that will let you customize the game a bit. The list of those variables is as follows:

- `BOX_OPEN_DELAY` and `BANKER_PICKUP_DELAY` (default: `3`) - These are both delays in seconds to wait before the host opens up a box/answers the banker's call.

- `BOX_COUNT` (default: `26`) - The amount of boxes to have in the game.

- `CURRENCY_SYMBOL` (default: `$`) - The currency symbol to use, such as $ or &pound;.

- `VALUES` (`tuple`, default: American Deal Or No Deal) - The values to be randomly put inside each box.

- `BANKER_OFFER_FREQUENCY` (default: `4`) - How many turns the banker will wait for each offer.

- `POSITIVE` (`tuple`) - List of responses for when the player makes a good choice.

- `NEGATIVE` (`tuple`) - List of responses for when the player makes a bad choice.

- Banker Formula Options - Will divide the mean of all remaining values on the board by these numbers (eg. `mean/7`), depending on if it's the first, second, or final third (&frac13;) of the game

- - `FIRST_BANKER_OFFER` (default: `8`) - Division number for the first third of the game
- - `SECOND_BANKER_OFFER` (default: `7`) - Division number for the second third of the game
- - `THIRD_BANKER_OFFER` (default: `1.75`) - Division number for the final third of the game