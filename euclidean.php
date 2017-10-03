<?php
/*
calculate GCD of two number
 */
function gcd($a, $b){
	if($b == 0) return $a;
	else return gcd($b, $a%$b);
}

// sample
//gcd(50, 60);

?>