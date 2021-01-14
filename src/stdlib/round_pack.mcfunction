#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]
#tellraw @a [{"score": {"name": "$exp", "objective": "namespace"}}]
#tellraw @a [{"score": {"name": "$sign", "objective": "namespace"}}]
execute unless score $exp namespace matches 0..252 run function namespace:round_pack1

scoreboard players operation $rb namespace = $sig namespace
# rb&0x7F == rb%0x80, due to the law
scoreboard players operation $rb namespace %= $128 namespace

# sig = (sig + 0x40)>>7
scoreboard players add $sig namespace 64
execute store result score $signn namespace if score $sig namespace matches ..-1
execute if score $signn namespace matches 1 run scoreboard players operation $sig namespace += $-inf namespace
scoreboard players operation $sig namespace /= $128 namespace
execute if score $signn namespace matches 1 run scoreboard players add $sig namespace 16777216
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]

# ! (roundBits ^ 0x40) = (roundBits ^ 0x40) == 0 = roundBits == 0x40
# a & ~0 = a, a & ~1 = 2*(a/2)
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]
execute if score $rb namespace matches 64 run scoreboard players operation $sig namespace /= $2 namespace
execute if score $rb namespace matches 64 run scoreboard players operation $sig namespace *= $2 namespace
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]

execute if score $sig namespace matches 0 run scoreboard players set $exp namespace 0
#tellraw @a [{"score": {"name": "$exp", "objective": "namespace"}}]
scoreboard players operation $sign namespace *= $-inf namespace
scoreboard players operation $out namespace = $sign namespace
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]
#scoreboard players operation $sig namespace %= $8388608 namespace
#tellraw @a [{"score": {"name": "$exp", "objective": "namespace"}}]
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]
scoreboard players operation $exp namespace *= $8388608 namespace
scoreboard players operation $out namespace += $exp namespace
scoreboard players operation $out namespace += $sig namespace