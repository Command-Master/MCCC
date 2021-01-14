execute store result score $search1 namespace run scoreboard players operation $search2 namespace = $index namespace
scoreboard players operation $search1 namespace /= $1024 namespace
scoreboard players remove $search1 namespace 524288
data modify storage namespace:main alloc[].selected set value 0
function namespace:tree/alloc_select
scoreboard players operation $search2 namespace %= $1024 namespace
function namespace:tree/alloc_set