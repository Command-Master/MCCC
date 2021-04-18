scoreboard players operation $exp namespace = $expa namespace
scoreboard players operation $exp namespace -= $expb namespace
scoreboard players add $exp namespace 126
scoreboard players add $siga namespace 8388608
scoreboard players add $sigb namespace 8388608
execute if score $siga namespace < $sigb namespace run scoreboard players remove $exp namespace 1
execute if score $siga namespace < $sigb namespace run scoreboard players operation $siga namespace *= $2 namespace
scoreboard players operation $siga namespace *= $128 namespace
scoreboard players operation $sigb namespace *= $256 namespace
#tellraw @a [{"score": {"name": "$siga", "objective": "namespace"}}, " ", {"score": {"name": "$sigb", "objective": "namespace"}}]
function namespace:float_div4
# answer in $r0

scoreboard players operation $aa namespace = $siga namespace
scoreboard players operation $aa namespace /= $65536 namespace
scoreboard players operation $aa namespace %= $65536 namespace
scoreboard players operation $ba namespace = $siga namespace
scoreboard players operation $ba namespace %= $65536 namespace

scoreboard players operation $ab namespace = $r0 namespace
scoreboard players operation $ab namespace /= $65536 namespace
scoreboard players operation $ab namespace %= $65536 namespace
scoreboard players operation $bb namespace = $r0 namespace
scoreboard players operation $bb namespace %= $65536 namespace

scoreboard players operation $ac namespace = $aa namespace
scoreboard players operation $ac namespace *= $ab namespace
# ad = aa
scoreboard players operation $aa namespace *= $bb namespace

scoreboard players operation $bc namespace = $ba namespace
scoreboard players operation $bc namespace *= $ab namespace
# bd = ba
scoreboard players operation $ba namespace *= $bb namespace

scoreboard players operation $sig namespace = $ac namespace
scoreboard players operation $t1 namespace = $aa namespace
scoreboard players operation $t1 namespace /= $65536 namespace
scoreboard players operation $t1 namespace %= $65536 namespace
scoreboard players operation $sig namespace += $t1 namespace

scoreboard players operation $t1 namespace = $bc namespace
scoreboard players operation $t1 namespace /= $65536 namespace
scoreboard players operation $t1 namespace %= $65536 namespace
scoreboard players operation $sig namespace += $t1 namespace

scoreboard players operation $aa namespace %= $65536 namespace
scoreboard players operation $bc namespace %= $65536 namespace
scoreboard players operation $aa namespace += $bc namespace

scoreboard players operation $ba namespace /= $65536 namespace
scoreboard players operation $ba namespace %= $65536 namespace

scoreboard players operation $aa namespace += $ba namespace

scoreboard players operation $aa namespace /= $65536 namespace
scoreboard players operation $aa namespace %= $65536 namespace

scoreboard players operation $sig namespace += $aa namespace

scoreboard players add $sig namespace 2

#tellraw @a [{"score": {"name": "$sign", "objective": "namespace"}}," ", {"score": {"name": "$exp", "objective": "namespace"}}, " ", {"score": {"name": "$sig", "objective": "namespace"}}]
function namespace:round_pack