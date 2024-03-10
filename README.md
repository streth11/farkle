# Farkle dice game monte carlo simulator


# Strategy Results
Strategy: SingleRoll (Baseline)
- Mean points: 419.4
- Probability Farkle: 0.019

Strategy: EndOn5Strategy
- Mean points: 394.9
- Probability Farkle: 0.4835

Strategy: EndOn4Strategy
- Mean points: 508.8
- Probability Farkle: 0.2225

Strategy: LeaveTriplet2sStrategy
- Mean points: 502.6
- Probability Farkle: 0.2375

Strategy: EndOn45ScoreDep
- Mean points: 435.6
- Probability Farkle: 0.5765

Strategy: RerollForTripletsMax1
- Mean points: 398.9
- Probability Farkle: 0.505

Strategy: RerollForTripletsFill
- Mean points: 371.8
- Probability Farkle: 0.5085

Strategy: CombinationStrategy (EndOn4Strategy, RerollForTripletsMax1, LeaveTriplet2sStrategy)
Mean points: 492.9
Probability Farkle: 0.341
