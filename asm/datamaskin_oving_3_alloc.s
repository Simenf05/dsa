# Denne filen inneholder skjelettet til Oppgave 1 på Praktisk Øving 3 i TDT4160
j _tests

#
# malloc er en funksjon som brukes for å allokere en sammenhengende blokk med minne.
# Kalles med a0 lik antall bytes du ønsker å allokere.
# Returnerer addressen til første byte i allokeringen i a0.
#
malloc:
    # Hent adressen til _heap_end
    la t0, _heap_end
    # Les den gamle slutten på heapen
    lw t1, 0(t0)
    # Sett til side a0 bytes
    add t2, t1, a0
    # Skriv den nye slutten på heapen
    sw t2, 0(t0)
    # Si ifra om at vi ønsker en større heap
    mv a0, t2
    li a7, 214 # brk-syscallet setter slutten på heapen
    ecall
    # Returner en peker til den nye allokeringen
    mv a0, t1
    ret

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Denne funksjonen skal allokere en liste bestående av N 32-bits tall.
# Listen skal bestå av tallene 1 til og med N.
# Tallet N er gitt som parameter i register a0.
# Adressen til første element i den allokerte listen skal returneres i register a0.
allocate_sequence:

    # Denne oppgaven handler først og fremst om å kalle malloc.
    # Husk at malloc tar inn antall *bytes* som skal allokeres.

    # Før du kaller malloc må du passe på at du har lagrer ra-registret,
    # slik at du får til å gjenopprette ra og returnere fra denne funksjonen.

    # Du vil måtte bevare tallet N, også etter kallet til malloc.
    # Dette kan du gjøre i et ABI-bevart register,
    # men da må du til gjengjeld passe på at du gjenoppretter verdien som lå der fra før.

    # Du må også passe på at sp-registret blir gjenopprettet,
    # og at du ikke tukler med verdier på stakken som befinner seg over sp.

    # TODO: Implementasjon

    # Forlater allocate_sequence her
    ret

########################################################################################
######################## Skriv koden din over denne linja ##############################
########################################################################################

_tests:
    # Setter ABI-bevarte registre til 77
    li s0, 77
    li s1, 77
    li s2, 77
    li s3, 77
    li s4, 77
    li s5, 77
    li s6, 77
    li s7, 77
    li s8, 77
    li s9, 77
    li s10, 77
    li s11, 77

    # Skriver 4 stykk 77 til stakken
    addi sp, sp, 16
    sw s0, 0(sp)
    sw s0, 4(sp)
    sw s0, 8(sp)
    sw s0, 12(sp)

    li a0, 10
    call allocate_sequence

    # Sjekker at listen er den første allokeringen gjort
    la t1, _bss_end
    bne t1, a0, _list_allocation_wrong

    # Sjekker at størrelsen på allokeringen er riktig
    lw t2, _heap_end
    sub t2, t2, t1
    li t3, 40
    bne t2, t3, _list_allocation_wrong_size

    # Sjekker at listen består av tallene fra 1 til 10
    mv t0, a0
    li t1, 1
    li t2, 10
_check_loop:
    bgt t1, t2, _check_loop_done
    lw t3, 0(t0)
    bne t1, t3, _list_wrong
    addi t1, t1, 1
    addi t0, t0, 4
    j _check_loop
_check_loop_done:

    # Sjekker at ingen av de ABI-bevarte registrene har blitt tuklet med
    li t0, 77
    bne s0, t0, _abi_clobbered
    bne s1, t0, _abi_clobbered
    bne s2, t0, _abi_clobbered
    bne s3, t0, _abi_clobbered
    bne s4, t0, _abi_clobbered
    bne s5, t0, _abi_clobbered
    bne s6, t0, _abi_clobbered
    bne s7, t0, _abi_clobbered
    bne s8, t0, _abi_clobbered
    bne s9, t0, _abi_clobbered
    bne s10, t0, _abi_clobbered
    bne s11, t0, _abi_clobbered

    # Sjekker at sp er på riktig sted og stakken er bevart
    lw t1, 0(sp)
    lw t2, 4(sp)
    lw t3, 8(sp)
    lw t4, 12(sp)
    bne t1, t0, _stack_clobbered
    bne t2, t0, _stack_clobbered
    bne t3, t0, _stack_clobbered
    bne t4, t0, _stack_clobbered

    j _all_tests_passed

_list_allocation_wrong:
    la a0, _list_allocation_wrong_str
    li a7, 4 # Print string
    ecall
    j _abort

_list_allocation_wrong_size:
    la a0, _list_allocation_wrong_size_str
    li a7, 4 # Print string
    ecall
    j _abort

_list_wrong:
    la a0, _list_wrong_str
    li a7, 4 # Print string
    ecall

    la a0, _list_wrong_got_str
    li a7, 4 # Print string
    ecall
    mv a0, t3
    li a7, 1 # Print int
    ecall

    la a0, _list_wrong_expected_str
    li a7, 4 # Print string
    ecall
    mv a0, t1
    li a7, 1 # Print int
    ecall

    j _abort

_abi_clobbered:
    la a0, _abi_clobbered_str
    li a7, 4 # Print string
    ecall
    j _abort

_stack_clobbered:
    la a0, _stack_clobbered_str
    li a7, 4 # Print string
    ecall
    j _abort

_abort:
    # Exit med kode 1
    li a0, 1
    li a7, 93
    ecall

_all_tests_passed:
    la a0, _all_tests_passed_str
    li a7, 4 # Print string
    ecall

    # Exit med kode 0
    li a7, 10
    ecall

# Heapen starter der bss-segmentet slutter
.bss
_bss_end: .zero 0

# Globale variabler
.data
_heap_end: .word _bss_end

_list_allocation_wrong_str: .string "Returadressen kommer ikke fra malloc"
_list_allocation_wrong_size_str: .string "Allokeringen har feil størrelse"
_list_wrong_str: .string "Den returnerte listen inneholder ikke tallene fra 1 til 10!"
_list_wrong_got_str:  .string "\nFikk: "
_list_wrong_expected_str:  .string "\nForventet: "
_abi_clobbered_str: .string "ABI-bevarte registre ble ikke bevart!"
_stack_clobbered_str: .string "Stakken ble ikke bevart!"
_all_tests_passed_str: .string "Testen var vellykket!"
