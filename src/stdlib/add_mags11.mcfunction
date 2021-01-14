execute store result score $sign namespace if score $aval namespace matches ..-1
scoreboard players operation $exp namespace = $expa namespace
scoreboard players set $sig namespace 16777216
scoreboard players operation $sig namespace += $siga namespace
scoreboard players operation $sig namespace += $sigb namespace
scoreboard players operation $m2 namespace = $sig namespace
scoreboard players operation $m2 namespace %= $2 namespace
execute if score $m2 namespace matches 0 if score $exp namespace matches ..253 run function namespace:add_mags111
scoreboard players operation $sig namespace *= $64 namespace