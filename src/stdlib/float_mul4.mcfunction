# input: $siga, $sigb
# output: $sig, containing sigA*sigB >> 32 + thing
scoreboard players operation $al namespace = $siga namespace
scoreboard players operation $al namespace %= $65536 namespace
scoreboard players operation $bl namespace = $sigb namespace
scoreboard players operation $bl namespace %= $65536 namespace

execute store result score $signn namespace if score $siga namespace matches ..-1
scoreboard players operation $ah namespace = $siga namespace
execute if score $signn namespace matches 1 run scoreboard players operation $ah namespace += $-inf namespace
scoreboard players operation $ah namespace /= $65536 namespace
execute if score $signn namespace matches 1 run scoreboard players add $ah namespace 32768

execute store result score $signn namespace if score $sigb namespace matches ..-1
scoreboard players operation $bh namespace = $sigb namespace
execute if score $signn namespace matches 1 run scoreboard players operation $bh namespace += $-inf namespace
scoreboard players operation $bh namespace /= $65536 namespace
execute if score $signn namespace matches 1 run scoreboard players add $bh namespace 32768

#tellraw @a [{"score": {"name": "$ah", "objective": "namespace"}}, " ", {"score": {"name": "$al", "objective": "namespace"}}]

scoreboard players operation $p00 namespace = $al namespace
scoreboard players operation $p00 namespace *= $bl namespace

scoreboard players operation $p10 namespace = $ah namespace
scoreboard players operation $p10 namespace *= $bl namespace

scoreboard players operation $p01 namespace = $al namespace
scoreboard players operation $p01 namespace *= $bh namespace

scoreboard players operation $p11 namespace = $ah namespace
scoreboard players operation $p11 namespace *= $bh namespace

scoreboard players operation $low namespace = $p00 namespace

scoreboard players operation $sig namespace = $p11 namespace

scoreboard players operation $temp namespace = $p01 namespace
execute store result score $signn namespace if score $p01 namespace matches ..-1
execute if score $signn namespace matches 1 run scoreboard players operation $temp namespace += $-inf namespace
scoreboard players operation $temp namespace /= $65536 namespace
execute if score $signn namespace matches 1 run scoreboard players add $temp namespace 32768
scoreboard players operation $sig namespace += $temp namespace

scoreboard players operation $temp namespace = $p10 namespace
execute store result score $signn namespace if score $p10 namespace matches ..-1
execute if score $signn namespace matches 1 run scoreboard players operation $temp namespace += $-inf namespace
scoreboard players operation $temp namespace /= $65536 namespace
execute if score $signn namespace matches 1 run scoreboard players add $temp namespace 32768
scoreboard players operation $sig namespace += $temp namespace

#tellraw @a [{"score": {"name": "$p11", "objective": "namespace"}}, " ", {"score": {"name": "$p01", "objective": "namespace"}}, " ", {"score": {"name": "$p10", "objective": "namespace"}}]

scoreboard players operation $p01 namespace *= $65536 namespace
scoreboard players operation $low namespace += $p01 namespace

# if low < p01: high++
scoreboard players set $compare namespace -1
execute if score $low namespace matches ..-1 if score $p01 namespace matches ..-1 run scoreboard players operation $compare namespace = $low namespace
execute if score $low namespace matches ..-1 if score $p01 namespace matches ..-1 run scoreboard players operation $compare namespace -= $p01 namespace
execute if score $low namespace matches 0.. if score $p01 namespace matches ..-1 run scoreboard players set $compare namespace 1
execute if score $low namespace matches 0.. if score $p01 namespace matches 0.. run scoreboard players operation $compare namespace = $low namespace
execute if score $low namespace matches 0.. if score $p01 namespace matches 0.. run scoreboard players operation $compare namespace -= $p01 namespace
execute if score $compare namespace matches ..-1 run scoreboard players add $sig namespace 1

scoreboard players operation $p10 namespace *= $65536 namespace
scoreboard players operation $low namespace += $p10 namespace

# if low < p10: high++
scoreboard players set $compare namespace -1
execute if score $low namespace matches ..-1 if score $p10 namespace matches ..-1 run scoreboard players operation $compare namespace = $low namespace
execute if score $low namespace matches ..-1 if score $p10 namespace matches ..-1 run scoreboard players operation $compare namespace -= $p10 namespace
execute if score $low namespace matches 0.. if score $p10 namespace matches ..-1 run scoreboard players set $compare namespace 1
execute if score $low namespace matches 0.. if score $p10 namespace matches 0.. run scoreboard players operation $compare namespace = $low namespace
execute if score $low namespace matches 0.. if score $p10 namespace matches 0.. run scoreboard players operation $compare namespace -= $p10 namespace
execute if score $compare namespace matches ..-1 run scoreboard players add $sig namespace 1

#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]

# (a & (1<<32 - 1)) != 0
scoreboard players operation $m2 namespace = $sig namespace
scoreboard players operation $m2 namespace %= $2 namespace
execute unless score $low namespace matches 0 if score $m2 namespace matches 1 run scoreboard players add $sig namespace 1

# scoreboard players operation $sig namespace %= $8388608 namespace