execute if score $expa namespace matches 255 run scoreboard players set $out namespace 2143289344
execute if score $expa namespace matches 255 run scoreboard players set $r namespace 1
scoreboard players operation $sigdiff namespace = $siga namespace
scoreboard players operation $sigdiff namespace -= $sigb namespace
execute if score $sigdiff namespace matches 0 run scoreboard players set $out namespace 0
execute if score $sigdiff namespace matches 0 run scoreboard players set $r namespace 1
execute if score $r namespace matches 0 run function namespace:sub_mags11