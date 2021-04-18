function namespace:tree/setjmp_copy
data modify storage namespace:main rec set from storage namespace:main stemps[1]
data modify storage namespace:main lstack set from storage namespace:main stemps[0]
scoreboard players operation $r0 namespace = $l2 namespace
execute if data storage namespace:main rec[0] run function namespace:resume
gamerule maxCommandChainLength 2