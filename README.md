#A compiler from the scratch:

Refer to this document for more information.

https://www.overleaf.com/read/vmcjpfhqmkwr

I am still developing and refactorizing the code.


Find the Smoke test in the parser_SSA-....ipnyb


## To do: 
Markup : 
	*ok: deal with a= a+b+c+d+a * b*c*d

	*deal with a= 1:
	     *Addi for now!

	*ok: complete the while SSA generator
	    *need to refactorize the code!
	    *need to check: if it works for nested while and if: not now! the bb number is wrong for now(return path)!
	    *check for nested if/while almost correct! need to check more

	*remove redundant computations: a<-x+y  b<-x+y
	*make 'live' graph of the SSA variables
	*deal with arrays
	*deal with functions/procedures: 
	    *function BB: ok, 
	    *call
	    *return value
	*deal with reserved functions: write, read,...
	*deal with uninitilized variables
	*maybe the list of SSA_table is wrong when I merge them in joint/merge bbs. 
	    *it depends on how I use it for the later step(make 'live' graph of the SSA variables)
