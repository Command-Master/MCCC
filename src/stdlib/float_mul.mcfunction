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

execute store result score $signa namespace if score $aval namespace matches ..-1
execute store result score $signb namespace if score $bval namespace matches ..-1
scoreboard players operation $sign namespace = $signa namespace
scoreboard players operation $sign namespace += $signb namespace

# technically not required, but if it is I don't wanna find this bug
scoreboard players operation $sign namespace %= $2 namespace

#TODO: handle infinities and NaNs
execute if score $expa namespace matches 255 run tellraw @a ["bad number :cry:", {"score": {"name":"$aval", "objective": "namespace"}}]
execute if score $expb namespace matches 255 run tellraw @a ["bad number :cry:", {"score": {"name":"$bval", "objective": "namespace"}}]

execute if score $expa namespace matches 0 run function namespace:float_mul1
execute if score $expb namespace matches 0 run function namespace:float_mul2

execute if score $r namespace matches 0 run function namespace:float_mul3