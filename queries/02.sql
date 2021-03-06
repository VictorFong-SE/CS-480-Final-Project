SELECT red.red{1} as {1}, count(red.red{1}) as totalPlays
FROM matches2020 red, matches2020 blue
WHERE red.red{1} = blue.blue{1}
GROUP BY red.red{1}
ORDER BY totalPlays desc; #done
-- gets the most played character given a role. This parses both red and blue side.
# SELECT red.redadc as ADC,
#        count(red.redadc) as totalPlays
# FROM matches2020 red, matches2020 blue
# WHERE red.redadc = blue.blueadc
# GROUP BY red.redadc
# ORDER BY totalPlays desc;