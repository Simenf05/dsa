	.file	"dijkstra.c"
	.text
	.globl	dijkstra
	.type	dijkstra, @function
dijkstra:
.LFB6:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$16, %edi
	call	malloc
	movq	%rax, -8(%rbp)
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	dijkstra, .-dijkstra
	.section	.rodata
.LC0:
	.string	"%d "
	.text
	.globl	print_graph
	.type	print_graph, @function
print_graph:
.LFB7:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$40, %rsp
	.cfi_offset 3, -24
	movl	%edi, -36(%rbp)
	movq	%rsi, -48(%rbp)
	movl	-36(%rbp), %ebx
	movslq	%ebx, %rax
	subq	$1, %rax
	movq	%rax, -32(%rbp)
	movl	$0, -20(%rbp)
	jmp	.L3
.L6:
	movl	$0, -24(%rbp)
	jmp	.L4
.L5:
	movl	-20(%rbp), %eax
	movslq	%eax, %rdx
	movslq	%ebx, %rax
	imulq	%rdx, %rax
	leaq	0(,%rax,4), %rdx
	movq	-48(%rbp), %rax
	addq	%rax, %rdx
	movl	-24(%rbp), %eax
	cltq
	movl	(%rdx,%rax,4), %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	addl	$1, -24(%rbp)
.L4:
	movl	-24(%rbp), %eax
	cmpl	-36(%rbp), %eax
	jl	.L5
	movl	$10, %edi
	call	putchar
	addl	$1, -20(%rbp)
.L3:
	movl	-20(%rbp), %eax
	cmpl	-36(%rbp), %eax
	jl	.L6
	nop
	nop
	movq	-8(%rbp), %rbx
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	print_graph, .-print_graph
	.globl	main
	.type	main, @function
main:
.LFB8:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$136, %rsp
	.cfi_offset 3, -24
	movl	$6, -32(%rbp)
	movl	$0, -112(%rbp)
	movl	$1, -108(%rbp)
	movl	$1, -104(%rbp)
	movl	$2, -100(%rbp)
	movl	$2, -96(%rbp)
	movl	$3, -92(%rbp)
	movl	$3, -88(%rbp)
	movl	$4, -84(%rbp)
	movl	$4, -80(%rbp)
	movl	$5, -76(%rbp)
	movl	$5, -72(%rbp)
	movl	$0, -68(%rbp)
	movl	$1, -144(%rbp)
	movl	$2, -140(%rbp)
	movl	$3, -136(%rbp)
	movl	$4, -132(%rbp)
	movl	$5, -128(%rbp)
	movl	$1, -124(%rbp)
	movl	-32(%rbp), %ebx
	movslq	%ebx, %rax
	subq	$1, %rax
	movq	%rax, -40(%rbp)
	movl	-32(%rbp), %eax
	movslq	%eax, %rdx
	movl	-32(%rbp), %eax
	cltq
	imulq	%rdx, %rax
	salq	$2, %rax
	movq	%rax, %rdi
	call	malloc
	movq	%rax, -48(%rbp)
	movl	$0, -20(%rbp)
	jmp	.L8
.L11:
	movl	$0, -24(%rbp)
	jmp	.L9
.L10:
	movl	-20(%rbp), %eax
	movslq	%eax, %rdx
	movslq	%ebx, %rax
	imulq	%rdx, %rax
	leaq	0(,%rax,4), %rdx
	movq	-48(%rbp), %rax
	addq	%rax, %rdx
	movl	-24(%rbp), %eax
	cltq
	movl	$0, (%rdx,%rax,4)
	addl	$1, -24(%rbp)
.L9:
	movl	-24(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L10
	addl	$1, -20(%rbp)
.L8:
	movl	-20(%rbp), %eax
	cmpl	-32(%rbp), %eax
	jl	.L11
	movl	$0, -28(%rbp)
	jmp	.L12
.L13:
	movl	-28(%rbp), %eax
	cltq
	movl	-112(%rbp,%rax,4), %eax
	movl	%eax, -52(%rbp)
	movl	-28(%rbp), %eax
	addl	$1, %eax
	cltq
	movl	-112(%rbp,%rax,4), %eax
	movl	%eax, -56(%rbp)
	movl	-28(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, -60(%rbp)
	movl	-52(%rbp), %eax
	movslq	%eax, %rdx
	movslq	%ebx, %rax
	imulq	%rdx, %rax
	leaq	0(,%rax,4), %rdx
	movq	-48(%rbp), %rax
	leaq	(%rdx,%rax), %rcx
	movl	-60(%rbp), %eax
	cltq
	movl	-144(%rbp,%rax,4), %edx
	movl	-56(%rbp), %eax
	cltq
	movl	%edx, (%rcx,%rax,4)
	addl	$2, -28(%rbp)
.L12:
	movl	-28(%rbp), %eax
	cmpl	$11, %eax
	jbe	.L13
	movq	-48(%rbp), %rdx
	movl	-32(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	print_graph
	movl	$0, %eax
	call	dijkstra
	movl	$0, %eax
	movq	-8(%rbp), %rbx
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	main, .-main
	.ident	"GCC: (GNU) 14.3.1 20251022 (Red Hat 14.3.1-4)"
	.section	.note.GNU-stack,"",@progbits
