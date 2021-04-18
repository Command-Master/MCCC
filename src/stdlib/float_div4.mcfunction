scoreboard players operation $index namespace = $sigb namespace
scoreboard players operation $index namespace /= $134217728 namespace
scoreboard players operation $index namespace %= $16 namespace
# set app1 to 1k1s[index], set r0 to 1k0s[index]
#tellraw @a {"score": {"name": "$index", "objective": "namespace"}}
function namespace:tree/approx_index
#tellraw @a [{"score": {"name": "$app1", "objective": "namespace"}}, " ", {"score": {"name": "$r0", "objective": "namespace"}}]

scoreboard players operation $eps namespace = $sigb namespace
scoreboard players operation $eps namespace /= $2048 namespace
scoreboard players operation $eps namespace %= $65536 namespace
#tellraw @a {"score": {"name": "$eps", "objective": "namespace"}}
scoreboard players operation $eps namespace *= $app1 namespace
scoreboard players operation $eps namespace /= $1048576 namespace
scoreboard players operation $eps namespace %= $4096 namespace
scoreboard players operation $r0 namespace -= $eps namespace
scoreboard players operation $r0 namespace %= $65536 namespace

#tellraw @a {"score": {"name": "$r0", "objective": "namespace"}}


# start u64 mul u64 r0 * sigb
scoreboard players operation $bl namespace = $sigb namespace
scoreboard players operation $bl namespace %= $65536 namespace
scoreboard players operation $bh namespace = $sigb namespace
scoreboard players operation $bh namespace /= $65536 namespace
scoreboard players operation $bh namespace %= $65536 namespace
#tellraw @a [{"score": {"name": "$bl", "objective": "namespace"}}, " ", {"score": {"name": "$bh", "objective": "namespace"}}]
# ah = 0
# al = $r0
# p10 = 0
scoreboard players operation $p01 namespace = $r0 namespace
scoreboard players operation $p01 namespace *= $bh namespace
# p11 = 0
scoreboard players operation $high namespace = $p01 namespace
scoreboard players operation $high namespace /= $65536 namespace
scoreboard players operation $high namespace %= $65536 namespace
scoreboard players operation $low namespace = $bl namespace
scoreboard players operation $low namespace *= $r0 namespace
scoreboard players operation $p01 namespace *= $65536 namespace
scoreboard players operation $low namespace += $p01 namespace
scoreboard players operation $t1 namespace = $low namespace
scoreboard players operation $t1 namespace += $-inf namespace
scoreboard players operation $p01 namespace += $-inf namespace
execute if score $t1 namespace < $p01 namespace run scoreboard players add $high namespace 1
# end uint64 mul


scoreboard players operation $low namespace /= $128 namespace
scoreboard players operation $low namespace %= $33554432 namespace
scoreboard players operation $high namespace *= $33554432 namespace
scoreboard players operation $low namespace += $high namespace
#tellraw @a {"score": {"name": "$low", "objective": "namespace"}}
scoreboard players add $low namespace 1
scoreboard players operation $low namespace *= $-1 namespace
# sigma0 = low

scoreboard players operation $sigma0 namespace = $low namespace

#tellraw @a {"score": {"name": "$sigma0", "objective": "namespace"}}

# start u64 mul r0 * sigma0
scoreboard players operation $bl namespace = $sigma0 namespace
scoreboard players operation $bl namespace %= $65536 namespace
scoreboard players operation $bh namespace = $sigma0 namespace
scoreboard players operation $bh namespace /= $65536 namespace
scoreboard players operation $bl namespace %= $65536 namespace
# ah = 0
# al = $r0
# p10 = 0
scoreboard players operation $p01 namespace = $r0 namespace
scoreboard players operation $p01 namespace *= $bh namespace
# p11 = 0
scoreboard players operation $high namespace = $p01 namespace
scoreboard players operation $high namespace /= $65536 namespace
scoreboard players operation $high namespace %= $65536 namespace
scoreboard players operation $low namespace = $bl namespace
scoreboard players operation $low namespace *= $r0 namespace
scoreboard players operation $p01 namespace *= $65536 namespace
scoreboard players operation $low namespace += $p01 namespace
scoreboard players operation $t1 namespace = $low namespace
scoreboard players operation $t1 namespace += $-inf namespace
scoreboard players operation $p01 namespace += $-inf namespace
execute if score $t1 namespace < $p01 namespace run scoreboard players add $high namespace 1
# end uint64 mul

scoreboard players operation $low namespace /= $16777216 namespace
scoreboard players operation $low namespace %= $256 namespace
scoreboard players operation $high namespace *= $256 namespace
scoreboard players operation $low namespace += $high namespace
#tellraw @a {"score": {"name": "$low", "objective": "namespace"}}
scoreboard players operation $r0 namespace *= $65536 namespace
scoreboard players operation $r0 namespace += $low namespace

# r = r0
#tellraw @a {"score": {"name": "$r0", "objective": "namespace"}}

# can reuse bl and bh
scoreboard players operation $p10 namespace = $bh namespace
scoreboard players operation $p10 namespace *= $bl namespace
scoreboard players operation $bh namespace *= $bh namespace
scoreboard players operation $high namespace = $p01 namespace
scoreboard players operation $high namespace /= $65536 namespace
scoreboard players operation $high namespace %= $65536 namespace
scoreboard players operation $high namespace *= $2 namespace
scoreboard players operation $high namespace += $bh namespace
scoreboard players operation $low namespace = $bl namespace
scoreboard players operation $low namespace *= $bl namespace
scoreboard players operation $p10 namespace *= $65536 namespace
scoreboard players operation $low namespace += $p10 namespace
scoreboard players operation $t2 namespace = $low namespace
scoreboard players operation $t2 namespace += $-inf namespace
scoreboard players operation $t1 namespace = $p10 namespace
scoreboard players operation $t1 namespace += $-inf namespace
execute if score $t2 namespace < $t1 namespace run scoreboard players add $high namespace 1
scoreboard players operation $low namespace += $p10
scoreboard players operation $t2 namespace += $p10
execute if score $t2 namespace < $t1 namespace run scoreboard players add $high namespace 1

# $r0 * $high
scoreboard players operation $aa namespace = $r0 namespace
scoreboard players operation $aa namespace /= $65536 namespace
scoreboard players operation $aa namespace %= $65536 namespace
scoreboard players operation $ba namespace = $r0 namespace
scoreboard players operation $ba namespace %= $65536 namespace

scoreboard players operation $ab namespace = $high namespace
scoreboard players operation $ab namespace /= $65536 namespace
scoreboard players operation $ab namespace %= $65536 namespace
scoreboard players operation $bb namespace = $high namespace
scoreboard players operation $bb namespace %= $65536 namespace

scoreboard players operation $ac namespace = $aa namespace
scoreboard players operation $ac namespace *= $ab namespace
# ad = aa
scoreboard players operation $aa namespace *= $bb namespace

scoreboard players operation $bc namespace = $ba namespace
scoreboard players operation $bc namespace *= $ab namespace
# bd = ba
scoreboard players operation $ba namespace *= $bb namespace

scoreboard players operation $thigh namespace = $ac namespace
scoreboard players operation $t1 namespace = $aa namespace
scoreboard players operation $t1 namespace /= $65536 namespace
scoreboard players operation $t1 namespace %= $65536 namespace
scoreboard players operation $thigh namespace += $t1 namespace

scoreboard players operation $t1 namespace = $bc namespace
scoreboard players operation $t1 namespace /= $65536 namespace
scoreboard players operation $t1 namespace %= $65536 namespace
scoreboard players operation $thigh namespace += $t1 namespace

scoreboard players operation $aa namespace %= $65536 namespace
scoreboard players operation $bc namespace %= $65536 namespace
scoreboard players operation $aa namespace += $bc namespace

scoreboard players operation $ba namespace /= $65536 namespace
scoreboard players operation $ba namespace %= $65536 namespace

scoreboard players operation $aa namespace += $ba namespace

scoreboard players operation $aa namespace /= $65536 namespace
scoreboard players operation $aa namespace %= $65536 namespace

scoreboard players operation $thigh namespace += $aa namespace
# hmult end


scoreboard players operation $thigh namespace /= $65536 namespace
scoreboard players operation $thigh namespace %= $65536 namespace
scoreboard players operation $r0 namespace += $thigh namespace