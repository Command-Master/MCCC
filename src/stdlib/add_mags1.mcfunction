#say mags1
execute if score $expa namespace matches 0 run scoreboard players operation $out namespace = $aval namespace
execute if score $expa namespace matches 0 run scoreboard players operation $out namespace += $sigb namespace
execute if score $expa namespace matches 0 run scoreboard players set $r namespace 1
execute if score $expa namespace matches 255 run scoreboard players operation $out namespace = $aval namespace
execute if score $expa namespace matches 255 unless score $siga namespace matches 0 run tellraw @a {"text": "NaN is not a number!", "color": "red"}
execute if score $expa namespace matches 255 unless score $sigb namespace matches 0 run tellraw @a {"text": "NaN is not a number!", "color": "red"}
execute if score $expa namespace matches 255 run scoreboard players set $r namespace 1
execute if score $r namespace matches 0 run function namespace:add_mags11