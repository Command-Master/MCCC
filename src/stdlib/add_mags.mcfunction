scoreboard players set $r namespace 0
# get exponents:
scoreboard players operation $expa namespace = $aval namespace
scoreboard players operation $expa namespace /= $8388608 namespace
scoreboard players operation $expa namespace %= $256 namespace
scoreboard players operation $expb namespace = $bval namespace
scoreboard players operation $expb namespace /= $8388608 namespace
scoreboard players operation $expb namespace %= $256 namespace

# get significants
scoreboard players operation $siga namespace = $aval namespace
scoreboard players operation $siga namespace %= $8388608 namespace
scoreboard players operation $sigb namespace = $bval namespace
scoreboard players operation $sigb namespace %= $8388608 namespace

scoreboard players operation $expdiff namespace = $expa namespace
scoreboard players operation $expdiff namespace -= $expb namespace
execute if score $expdiff namespace matches 0 run function namespace:add_mags1
execute unless score $expdiff namespace matches 0 run function namespace:add_mags2
execute if score $r namespace matches 0 run function namespace:round_pack