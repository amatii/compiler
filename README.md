#A compiler from scratch:

Refer to this document for more information.

https://www.overleaf.com/read/vmcjpfhqmkwr

I am still developing and refactorizing the code.


Find the Smoke test in the parser_SSA-....ipnyb


## To do: 
* bug:
	* (4) and #49 are the same and considered as SSA number!

* make 'live' graph of the SSA variables
	* made the graph: how to eliminate dead code? I have to consider what program return, print, or write? https://www.seas.harvard.edu/courses/cs153/2018fa/lectures/Lec23-SSA.pdf oage 37: 1. stores into mem, performs I/O, returns from function, calls function that may have side effects •2. defines variable that is used in a live statement •3. is a conditional branch that affects whether a live statement is executed (i.e., live statement is control dependent on the branch)

	* implement graph coloring, or implement my own? (ask Franz)
	* how to implement 'While'? http://ssabook.gforge.inria.fr/latest/book.pdf page 96: The firstpass, very similar to traditional data-flow analysis, computes partial liveness setsby traversing the forward-CFG backwards. The second pass refines the partialliveness sets and computes the final solution by propagating forward along theloop nesting forest. For the sake of clarity, we first present the algorithm forreducible CFGs. Irreducible CFGs?can be handled with a slight variation of thealgorithm, with no need to modify the CFG itself.
	* how deal with phi?
	* what to do with the ones eliminated by CSE?
	* add move to the Phi: to the previous block?! where I have to add it?

* assigning registers:
	* what to do with the spill over?
	
* deal with arrays
* deal with functions/procedures: 
	* function BB: ok, 
		* call
		* return value
	* deal with reserved functions: write, read,...
	* how deal with Phi?
* deal with uninitilized variables
	* it depends on how I use it for the later step(make 'live' graph of the SSA variables)


## Done: 
* priority: While loop:
	* add BRA at the end of inside_loop_BB.: done
	* update the inside_loop SSA_number!!!!: done
* ok: deal with a= a+b+c+d+a+b*c 
* deal with assignment: (e.g. a = 1)
	* Addi for now!
* remove redundant computations: '< a<-x+y  b<-x+y >'
	* refactorize the code
	* I used two pass: one for finding the repeated op, and the second pass to replace the SSA_number: is it correct? or I have to follow the single pass emthod?
* bug detected and debugged
	* IF branch BRA to the beginning of the merge node, not the beggining of the ELSE branch
	* WHILE: solved updating the SSA number in the inside while branch, based on the Phi. have to check more.

## test and others: 
* make 'live' graph of the SSA variables
	* reversed the edges of CFG. then started with bb without input edge.(kind of lexical ordering!): done
	* what to do with the ones eliminated by CSE?: those SSA lines removed by CSE, wont be used later. so it is safe not to consider them in coloring.

* WHILE: solved updating the SSA number in the inside while branch, based on the Phi. have to check more.
* ok: complete the while SSA generator
	* need to refactorize the code!
	* need to check: if it works for nested while and if: not now! the bb number is wrong for now(return path)!
	* check for nested if/while almost correct! need to check more
* maybe the list of SSA_table is wrong when I merge them in joint/merge bbs. 
* CSE just take care of first block(entry block), not all the dominator BB: fixed: need to check more
