var a = 60,
	b=40,

	gcd = function(a, b){
		if(b == 0) return a;
		else return gcd(b, a%b);
	};

alert(gcd(a, b));