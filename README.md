Hockey Advanced Stats Interactive Chart

I believe that the now infamous hockey advanced statistic, most commonly known as "Corsi", is a highly flawed metric. A player's Corsi is calculated by looking at his/her team's shot attempts (shots on goal, wide, or blocked) in relation to the opposing team's shot attempts while this player is on the ice. For example, a player with a Corsi far above 50% may be considered above average because while the player is on the ice, the player's team is attempting more shots on the other team's net. Under such prism, Shot attempts are considered a proxy for puck possession and chance generation.

I feared that a player's Corsi statistic may not accurately describe actual high quality chance generation in reality. Players might be able to generate many low quality scoring chances by inflating their shot attempt stats with low quality shots from the perimeter. Furthermore, Corsi generally has an upper limit of 60%, meaning that even the "best" players still have to defend 40% of the time. What if a player with a 60% Corsi is a poor defender in the defensive zone and gives up more goals than average during that other 40% of the game?

I created a new statistic, called "Weighted Corsi Percentage", in an attempt to create a superior metric. Weighted Corsi is calculated by adding the percentage of goals forward to shot attempts forward with the percentage of goals against to shot attempts against. Therefore, a player with a poor Corsi may be considered to be an above average player if he/she is a strong defender as measured by the goals surrendered relative to the shot attempts against.

I created an interactive scatter plot so scouts can choose two statistics and plot them together to uncover any relationships in the data. I build this feature because I wished to display Weighted Corsi against "PDO" (shooting percentage + save percentage), a statistic widely regarded as a measure a player's luck. I wanted to see whether a player's "luck" affected his/her underlying possession statistics, or whether we had the causal arrow pointing in the wrong direction all along - ie. the player's ability drives his/her "luck" statistic.

Created by Jake MacNaughton (2018)
